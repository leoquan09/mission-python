room_nums = {
    'CS101': 3004,
    'CS102': 4501,
    'CS103': 6755,
    'NT110': 1244,
    'CM241': 1411
}

instructors = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

meeting_times = {
    'CS101': 'Haynes',
    'CS102': 'Alvarado',
    'CS103': 'Rich',
    'NT110': 'Burke',
    'CM241': 'Lee'
}

course = input('Enter a course number to get info on: ')

if course not in room_nums:
    print('Course not found')
else:
    print(f'Room number: {room_nums[course]}, instructor: {instructors[course]}, meeting time: {meeting_times[course]}')
