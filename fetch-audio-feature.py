import requests
import hashlib

class LastFMMetadata:
    def __init__(self, api_key):
        self.api_key = api_key  # Free from last.fm/api
        self.base_url = 'http://ws.audioscrobbler.com/2.0/'
    
    def search_track(self, artist, title):
        """Search for track metadata on Last.fm"""
        params = {
            'method': 'track.search',
            'track': title,
            'artist': artist,
            'api_key': self.api_key,
            'format': 'json',
            'limit': 1
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if 'results' in data and 'trackmatches' in data['results']:
                tracks = data['results']['trackmatches']['track']
                if tracks:
                    track = tracks[0] if isinstance(tracks, list) else tracks
                    return {
                        'lastfm_artist': track.get('artist'),
                        'lastfm_title': track.get('name'),
                        'lastfm_mbid': track.get('mbid')
                    }
        except Exception as e:
            print(f"Last.fm search failed: {e}")
        return {}