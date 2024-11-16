import React from 'react';
import './Result.css';

const GoogleNews = () => {
  const newsTiles = [
    { title: 'News 1', text: 'Breaking news about the company.' },
    { title: 'News 2', text: 'Company announces new product launch.' },
    { title: 'News 3', text: 'Company expands globally.' },
    { title: 'News 4', text: 'Company CEO speaks at conference.' },
    { title: 'News 5', text: 'Company reports record earnings.' },
    { title: 'News 6', text: 'New partnership announcement.' },
    { title: 'News 7', text: 'Company wins award for innovation.' },
    { title: 'News 8', text: 'Company receives environmental recognition.' },
    { title: 'News 9', text: 'Company enters new market segment.' },
    { title: 'News 10', text: 'Company makes strategic acquisition.' },
  ];

  return (
    <div className="google-news">
      <h2>Google News</h2>
      <div className="carousel">
        {newsTiles.map((tile, index) => (
          <div key={index} className="news-tile">
            <h3>{tile.title}</h3>
            <p>{tile.text}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GoogleNews;
