const fileInput = document.getElementById('audio');
const fileLabel = document.getElementById('audio-label');

fileInput.addEventListener('change', function() {
  fileLabel.textContent = fileInput.files[0].name;
});
