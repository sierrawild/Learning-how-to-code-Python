import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        
        # Sound folder path
        self.sound_folder = "sounds"
        
        # Load sound effects
        self.sounds = {}
        
        try:
            # Coin collection sound
            coin_path = os.path.join(self.sound_folder, "coin.wav")
            if os.path.exists(coin_path):
                self.sounds['coin'] = pygame.mixer.Sound(coin_path)
                self.sounds['coin'].set_volume(0.5)
            
            # Crash/collision sound
            crash_path = os.path.join(self.sound_folder, "crash.wav")
            if os.path.exists(crash_path):
                self.sounds['crash'] = pygame.mixer.Sound(crash_path)
                self.sounds['crash'].set_volume(0.7)
            
            # Plane engine/whoosh sound
            whoosh_path = os.path.join(self.sound_folder, "whoosh.wav")
            if os.path.exists(whoosh_path):
                self.sounds['whoosh'] = pygame.mixer.Sound(whoosh_path)
                self.sounds['whoosh'].set_volume(0.3)
            
            # Game over sound
            gameover_path = os.path.join(self.sound_folder, "gameover.wav")
            if os.path.exists(gameover_path):
                self.sounds['gameover'] = pygame.mixer.Sound(gameover_path)
                self.sounds['gameover'].set_volume(0.6)
            
            print(f"Loaded {len(self.sounds)} sound effects")
            
        except Exception as e:
            print(f"Error loading sounds: {e}")
        
        # Load background music
        try:
            music_path = os.path.join(self.sound_folder, "background_music.mp3")
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.4)
                print("Background music loaded")
            else:
                print(f"Music file not found: {music_path}")
        except Exception as e:
            print(f"Error loading music: {e}")
    
    def play_sound(self, sound_name):
        """Play a sound effect"""
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
    
    def play_music(self, loops=-1):
        """Start playing background music (loops=-1 means loop forever)"""
        try:
            pygame.mixer.music.play(loops)
        except:
            pass
    
    def stop_music(self):
        """Stop background music"""
        pygame.mixer.music.stop()
    
    def pause_music(self):
        """Pause background music"""
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        """Unpause background music"""
        pygame.mixer.music.unpause()
    
    def set_music_volume(self, volume):
        """Set music volume (0.0 to 1.0)"""
        pygame.mixer.music.set_volume(volume)
    
    def set_sound_volume(self, sound_name, volume):
        """Set volume for a specific sound effect (0.0 to 1.0)"""
        if sound_name in self.sounds:
            self.sounds[sound_name].set_volume(volume)