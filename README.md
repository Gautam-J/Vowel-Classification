

## About the Dataset:
### What is the 'Saarbruecken Voice Database'?

A collection of voice recordings from more than 2000 persons. One recording session contains the following recordings:

- Recording of the vowels [i, a, u] produced at normal, high and low pitch.
- Recordings of the vowels [i, a, u] with rising-falling pitch.


## Methodology
### Feature Extraction: 
- Extraction of features is a very important part in analyzing and finding relations between different things. The data provided of audio cannot be understood by the models directly to convert them into an understandable format feature extraction is used.


<h2> Recurrent Neural Network </h2>
<p>
For this data we have used a stateful LSTM thats allows us to simplify the overall network structure. All we need here is the LSTM layer followed by a Dense layer.
A single audio sample is fed to the network and a single sample is predicted. There is no need for a range of samples since the necessary information about the past signal is stored in the LSTM’s recurrent state.
It’s important to note that a skip connection is performed, where the input sample value is added to the output value. This way, the network only has to learn the difference between the output and the input. 





## Contributors
<a href="https://github.com/gautam-j/gautam-j/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gautam-j/gautam-j" />
</a>
<a href="https://github.com/brijes-h/brijes-h/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=brijes-h/brijes-h" />
</a>
<a href="https://github.com/Manishankar9977/Manishankar9977/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jahnavidarbhamulla/jahnavidarbhamulla" />
</a>
  <a href="https://github.com/jahnavidarbhamulla/jahnavidarbhamulla/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kruthim1304/kruthim1304" />
  <a href="https://github.com/jahnavidarbhamulla/jahnavidarbhamulla/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=pryanshukundu/pryanshukundu" />
</a>



  
## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

<p align="center">
	Made with :coffee: and :heart:
</p>




