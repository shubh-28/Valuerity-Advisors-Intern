import React from 'react';
import './Main.css';
import bgImg from '../images/bg-img.png'; // Import the image

const Main = () => {
  const landingStyle = {
    backgroundImage: `linear-gradient(to bottom, rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.85)), url(${bgImg})`,
  backgroundRepeat: 'no-repeat',
  backgroundPosition: 'center center',
  backgroundSize: 'cover',
  height: '70vh',
  margin: '50px',
  borderRadius: '20px',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  position: 'relative',
  overflow: 'hidden', // Ensure content stays within rounded edges
};

const glassMorphismStyle = {
  position: 'absolute',
  top: 0,
  left: 0,
  width: '100%',
  height: '100%',
  background: 'rgba(255, 255, 255, 0.05)', // Translucent overlay
  backdropFilter: 'blur(3.5px)', // Frosted glass effect
  borderRadius: 'inherit', // Match parent border radius
  zIndex: 1,
};

  return (
    <div className="home-page">
      {/* Landing Section */}
      <div style={landingStyle}>
      <div style={glassMorphismStyle}></div>
        <div className="overlay" style={{ zIndex: 2 }}>
          <h1 className="landing-title">Find Company Insights</h1>
          <div className="search-bar">
            <div className="search-container">
              <input
                type="text"
                placeholder="Search for a company..."
                className="search-input"
              />
              <button className="search-button">Search</button>
            </div>
          </div>
        </div>
      </div>

      {/* Section Heading */}
      <h2 className="section-heading">Uncover the companies you care about</h2>

      {/* Tiles Section */}
      <div className="tiles-section">
        <div className="tile">
          <h3>Tile 1</h3>
          <p>Details about the first company insight.</p>
        </div>
        <div className="tile">
          <h3>Tile 2</h3>
          <p>Details about the second company insight.</p>
        </div>
        <div className="tile">
          <h3>Tile 3</h3>
          <p>Details about the third company insight.</p>
        </div>
        {/* Add more tiles as needed */}
      </div>
    </div>
  );
};

export default Main;
