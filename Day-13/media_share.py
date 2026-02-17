media = [
    'beach.png',
    'waves.mp4',
    'birthday.jpg',
    'party.mp4',
    'mountain.jpeg',
    'dance.mp4',
    'sunset.png',
    'travel.mp4',
    'selfie.jpg',
    'concert.mp4'
]
photos=[]
videos=[]
print("---- Media List ----")
for i in media:
    if i.endswith('mp4'):
        videos.append(i)
    else:
        photos.append(i)
print('\n ---- photos ----')
for i in photos:
    print(i)
    
print('\n ---- videos ----')
for i in videos:
    print(i)

select=set(input("enter the files to share(using comma):").split(','))
for i in select:
    if i in media:
        print(f'{i}-sent')
    else:
        print(f'{i}- file not found')
