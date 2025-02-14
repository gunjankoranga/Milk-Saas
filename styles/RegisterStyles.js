import { StyleSheet, Dimensions } from 'react-native';

const { width, height } = Dimensions.get('window');

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0D47A1',  // Blue background for the whole screen
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 30,
    color: '#fff',
    textAlign: 'center',
    marginBottom: 20,
    fontWeight: 'bold',
    zIndex: 2,
  },
  whiteContainer: {
    width: '90%',
    backgroundColor: '#fff',
    borderRadius: 30,
    padding: 20,
    paddingTop: 40,
    elevation: 10,
    zIndex: 2,
    overflow: 'hidden',
  },
  waveTop: {
    position: 'absolute',
    top: -30,
    left: 0,
    right: 0,
    height: 60,
    backgroundColor: '#0D47A1',
    borderBottomLeftRadius: 100,
    borderBottomRightRadius: 100,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F1F1F1',
    borderRadius: 25,
    paddingHorizontal: 15,
    marginVertical: 10,
    width: '100%',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 10,
    elevation: 5,
  },
  input: {
    flex: 1,
    padding: 10,
  },
  button: {
    backgroundColor: '#0D47A1',
    borderRadius: 25,
    paddingVertical: 15,
    width: '100%',
    alignItems: 'center',
    marginVertical: 10,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
  },
  signInText: {
    color: '#757575',
    textAlign: 'center',
    marginTop: 20,
  },
  signInLink: {
    color: '#0D47A1',
    fontWeight: 'bold',
  },
});

export default styles;
