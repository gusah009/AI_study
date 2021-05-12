import logo from './logo.svg';
import './App.css';
import CanvasDraw from 'react-canvas-draw';
import { useRef, useState, useEffect } from 'react';
import { Container, Button, Grid } from '@material-ui/core';

function useWindowSize() {
  // Initialize state with undefined width/height so server and client renders match
  // Learn more here: https://joshwcomeau.com/react/the-perils-of-rehydration/
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  });

  useEffect(() => {
    // Handler to call on window resize
    function handleResize() {
      // Set window width/height to state
      setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    }

    // Add event listener
    window.addEventListener("resize", handleResize);

    // Call handler right away so state gets updated with initial window size
    handleResize();

    // Remove event listener on cleanup

    return () => window.removeEventListener("resize", handleResize);

  }, []); // Empty array ensures that effect is only run on mount

  return windowSize;
}

function App() {
  const width = useWindowSize().width;
  console.log(width);
  const canvasRef = useRef();
  const canvasConfig = {
    onChange: null,
    loadTimeOffset: 5,
    lazyRadius: 0,
    brushRadius: 12 * (window.innerWidth > 552 ? 1 : window.innerWidth < 240 ? 240 / 552 : window.innerWidth / 552),
    brushColor: "black",
    catenaryColor: "#0a0302",
    gridColor: "rgba(150,150,150,0.17)",
    hideGrid: true,
    canvasWidth: (window.innerWidth > 552 ? 552 : window.innerWidth < 240 ? 240 : (window.innerWidth - 32)),
    canvasHeight: (window.innerWidth > 552 ? 552 : window.innerWidth < 240 ? 240 : (window.innerWidth - 32)),
    disabled: false,
    imgSrc: "./",
    saveData: null,
    immediateLoading: false,
    hideInterface: false
  };

  function handleChangeData(e) {
    console.log(e);
  }

  function handleClearClick(e) {
    console.log(e);
  }

  return (
    <div className="App"  style={{backgroundColor : 'rgba(59, 130, 246, 0.5)'}}>
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <main>
        <Container maxWidth="sm">
          <CanvasDraw {...canvasConfig} ref={canvasRef} onChange={ handleChangeData }/>
          <div className="flex justify-between m-auto" style={{ width: canvasConfig.canvasWidth }}>
            <Button size="medium" variant="contained" color="secondary" onClick={ handleClearClick }>
              Clear
            </Button>
          </div>
        </Container>
      </main>
    </div>
  );
}

export default App;
