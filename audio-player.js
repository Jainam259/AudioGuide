// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Get DOM elements
    const audioElement = document.getElementById('audio-element');
    const playPauseButton = document.getElementById('play-pause');
    const volumeToggle = document.getElementById('volume-toggle');
    const volumeIndicator = document.getElementById('volume-indicator');
    
    // Make sure we have all required elements
    if (!audioElement || !playPauseButton || !volumeToggle || !volumeIndicator) {
        console.error('One or more required elements not found');
        return;
    }
    
    // Set initial values
    let isPlaying = false;
    let isHighVolume = true;
    const HIGH_VOLUME = 1.0; // 100%
    const LOW_VOLUME = 0.3;  // 30%
    
    // Set initial volume
    audioElement.volume = HIGH_VOLUME;
    
    // Play/Pause button functionality
    playPauseButton.addEventListener('click', function() {
        if (isPlaying) {
            audioElement.pause();
            playPauseButton.textContent = 'Play';
        } else {
            // Use a promise to handle play() since it returns a promise
            const playPromise = audioElement.play();
            
            if (playPromise !== undefined) {
                playPromise.then(_ => {
                    playPauseButton.textContent = 'Pause';
                })
                .catch(error => {
                    console.error('Error playing audio:', error);
                });
            }
        }
        isPlaying = !isPlaying;
    });
    
    // Volume toggle functionality
    volumeToggle.addEventListener('click', function() {
        try {
            if (isHighVolume) {
                // Switch to low volume
                audioElement.volume = LOW_VOLUME;
                volumeToggle.textContent = 'Volume: Low';
                volumeToggle.classList.add('low');
                volumeIndicator.textContent = 'Current Volume: 30%';
            } else {
                // Switch to high volume
                audioElement.volume = HIGH_VOLUME;
                volumeToggle.textContent = 'Volume: High';
                volumeToggle.classList.remove('low');
                volumeIndicator.textContent = 'Current Volume: 100%';
            }
            isHighVolume = !isHighVolume;
            console.log('Volume changed to:', audioElement.volume);
        } catch (error) {
            console.error('Error changing volume:', error);
        }
    });
    
    // Update display if the audio element's volume changes programmatically
    audioElement.addEventListener('volumechange', function() {
        const volumePercent = Math.round(audioElement.volume * 100);
        volumeIndicator.textContent = `Current Volume: ${volumePercent}%`;
        
        // Update the button text too
        if (audioElement.volume >= 0.5) {
            volumeToggle.textContent = 'Volume: High';
            volumeToggle.classList.remove('low');
            isHighVolume = true;
        } else {
            volumeToggle.textContent = 'Volume: Low';
            volumeToggle.classList.add('low');
            isHighVolume = false;
        }
    });
    
    // Listen for when audio is ready to play
    audioElement.addEventListener('canplaythrough', function() {
        console.log('Audio is ready to play');
    });
    
    // Listen for errors
    audioElement.addEventListener('error', function(e) {
        console.error('Error with audio element:', e);
    });
}); 