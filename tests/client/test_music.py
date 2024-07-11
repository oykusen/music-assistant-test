from typing import Any
from music_assistant.client.music import Music
from music_assistant.client.client import MusicAssistantClient
from music_assistant.common.models.media_items import Track
from music_assistant.common.models.media_items import Artist


class TestMusicAssistantClient(MusicAssistantClient):
    async def send_command(
            command: str,
            require_schema: int | None = None,
            **kwargs: Any,
            )-> dict:
            if command == "music/tracks/get_track":
                return {
                      "album_uri" : kwargs["album_uri"],
                      "item_id" : kwargs["item_id"],
                      "provider" : "test_provider",
                      "name" : "test_name",
                      "provider_mappings": [
                        {
                        "item_id": kwargs["item_id"],
                        "provider_domain": kwargs["provider_instance_id_or_domain"],
                        "provider_instance": "test_instance"
                        }
                      ],
                }
            elif command == "music/artists/get_artist":
                 return {
                      "item_id" : kwargs["item_id"],
                      "provider" : "test_provider",
                      "name" : "test_name",
                      "provider_mappings": [
                        {
                        "item_id": kwargs["item_id"],
                        "provider_domain": kwargs["provider_instance_id_or_domain"],
                        "provider_instance": "test_instance"
                        }
                      ],
                 }
            else:
                 return{
                      "item_id" : kwargs["item_id"],
                 }
    

            
            
    

# get_track function uses only send_command function from MusicAsistantClient
async def test_get_track() -> None:

      test_client = TestMusicAssistantClient
      test_music = Music(test_client)
      
      temp_track = await test_music.get_track(item_id="test_id",provider_instance_id_or_domain="test_provider_id",album_uri="test_album_uri")
      
      assert isinstance(temp_track,Track)
      assert temp_track.item_id == "test_id"
      # uri must be in this format: provider://track/item_id
      assert temp_track.uri == "test_provider://track/test_id"
      assert temp_track.name == "test_name"
      

     


async def test_get_artist() -> None:
    
    test_client = TestMusicAssistantClient
    test_music = Music(test_client)

    temp_artist = await test_music.get_artist("test_id", "test_provider_id")

    assert isinstance(temp_artist,Artist)
    assert temp_artist.item_id == "test_id"
    assert temp_artist.name == "test_name"
    # uri must be in this format: provider://artist/item_id     
    assert temp_artist.uri == "test_provider://artist/test_id"

      
      