from django.shortcuts import render, HttpResponse
from .models import Subtitles
import time
import requests


def time_reversal(time):
    hour, min, sec = time.split(':')
    hour, min, sec = int(float(hour)), int(float(min)), int(float(sec))
    return 3600 * hour + min * 60 + sec


def seconds_to_hms(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f"{hours}h{minutes}m{remaining_seconds}s"


def add_dialogs(start_number, result=[], max_sentences=7, distance=1, time_fan=[], gap_time=4,
                file_name='sunset_boulevard'):
    # 获取当前字幕
    initial_time = time_reversal(Subtitles.objects.filter(film_name=file_name, number=start_number)[0].start_time)
    if not time_fan:
        time_fan = [initial_time, initial_time]
    if len(result) >= max_sentences:
        return result
    pre_info = Subtitles.objects.filter(film_name=file_name, number=start_number + distance)
    post_info = Subtitles.objects.filter(film_name=file_name, number=start_number - distance)
    pre_lane = []
    post_lane = []
    if pre_info:
        start_time_ = time_reversal(pre_info[0].start_time)
        if abs(start_time_ - time_fan[0]) < gap_time and abs(initial_time - start_time_) < 15:
            time_fan[0] = start_time_
            pre_lane = [pre_info[0]]
    if post_info:
        start_time_ = time_reversal(post_info[0].start_time)
        if abs(start_time_ - time_fan[1]) < gap_time and abs(initial_time - start_time_) < 15:
            time_fan[1] = start_time_
            post_lane = [post_info[0]]

    result = pre_lane + result + post_lane
    if len(result) >= max_sentences or not (pre_lane + post_lane):
        return result
    return add_dialogs(start_number, result=result, max_sentences=max_sentences, distance=distance + 1,
                       time_fan=time_fan)


def search(request):
    t = time.time()
    query = request.GET.get('q', '')
    results = Subtitles.objects.filter(film_name="sunset_boulevard", text__icontains=query)
    if len(results) > 40:
        return render(request, 'engine/search.html', {'query': query, 'results': [], 'number_of_results': len(results),
                                                      'time_taken': f"{float(time.time() - t):.5f}",
                                                      'error_message': "Too many results, please exact keywords"})
    # 使用字典存储所有字幕以便快速查找
    for result in results:
        current_number = int(result.number)
        result.dialogs = []

        # 使用递归添加对话
        result.dialogs = add_dialogs(current_number, result=[result])
        result.dialogs.sort(key=lambda x: x.number)
        earliest_time = time_reversal(result.dialogs[0].start_time)
        result.start_play_time = seconds_to_hms(earliest_time)

    # 这里可以添加其他逻辑
    return render(request, 'engine/search.html', {'query': query, 'results': results,
                                                  'number_of_results': len(results),
                                                  'time_taken': f"{float(time.time() - t):.5f}"}, )


def delete(request):
    Subtitles.objects.all().delete()
    import time
    return HttpResponse(f'success,{time.time()}')


def video(request):
    video_ = requests.get("https://vimeo.com/api/oembed.json?url=https%3A//vimeo.com/1020879319&width=480&height=360")
    return render(request, 'engine/video.html', {'video_': video_})
