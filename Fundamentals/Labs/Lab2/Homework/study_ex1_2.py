from youtube_dl import YoutubeDL
# download video
dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# download audio
options = {
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])
#search and download video
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}
dl = YoutubeDL(options)
dl.download(['con điên TAMKA PKL'])
# search and download audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['em gai mua huong tram'])