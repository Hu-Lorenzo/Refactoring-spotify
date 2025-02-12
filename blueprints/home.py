from flask import Flask, redirect, request, url_for, render_template, session, Blueprint
from services.spotify_oauth import sp_oauth, get_spotify_object  
import spotipy  

home_bp = Blueprint('home', __name__)

@home_bp.route('/home')
def home():
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('auth.login')) 

    sp = get_spotify_object(token_info)  
    user_info = sp.current_user()
    playlists = sp.current_user_playlists()['items']

    return render_template('home.html', user_info=user_info, playlists=playlists)


@home_bp.route('/playlist/<playlist_id>')
def playlist(playlist_id):
    token_info = session.get('token_info', None)
    if not token_info:
        return redirect(url_for('auth.login'))  
    sp = get_spotify_object(token_info) 
    playlist_tracks = sp.playlist_items(playlist_id)

    tracks = [{
        'name': track['track']['name'],
        'artist': track['track']['artists'][0]['name'],
        'album': track['track']['album']['name'],
        'image': track['track']['album']['images'][0]['url'] if track['track']['album']['images'] else None
    } for track in playlist_tracks['items']]

    return render_template('playlist.html', tracks=tracks)
