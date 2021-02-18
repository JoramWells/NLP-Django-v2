from .modules import *

class SearchView:
    def __init__(self,keyword,min_videos):
        self.keyword = keyword
        self.min_videos =min_videos


    



    def postl(self,*args, **kwargs):
        transcripts_url = "data.csv"
        if self.keyword and self.min_videos:
            min_videos = int(self.min_videos)

            dataframe = read_data(transcripts_url)
            video_ids = tf_idf(self.keyword, dataframe, 'body', self.min_videos)
            video_urls = []

            for vid in video_ids:
                url = dataframe.loc[vid, 'id']
                video_urls.append(url)

            context = { 'videos': video_urls  }
            print(context )
            return video_urls
        return 0
