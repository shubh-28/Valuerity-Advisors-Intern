import './Result.css';
// import React, { useState } from 'react';


import React, { useState, useMemo, useEffect } from 'react';

const styles = {
  googleNews: {
    textAlign: 'center',
    maxWidth: '1500px',
    margin: '0 auto',
    padding: '0 20px'
  },
  headerContainer: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '1.5rem',
    padding: '0 50px'
  },
  title: {
    fontSize: '2rem',
    margin: 0
  },
  timeFilter: {
    padding: '8px 12px',
    borderRadius: '4px',
    border: '1px solid #ddd',
    backgroundColor: 'white',
    fontSize: '1rem',
    cursor: 'pointer',
    outline: 'none'
  },
  carouselContainer: {
    position: 'relative',
    padding: '0 50px'
  },
  newsContainer: {
    display: 'flex',
    gap: '20px',
    transition: 'all 0.3s ease'
  },
  newsTile: {
    flex: 1,
    background: '#fff',
    padding: '1rem',
    borderRadius: '8px',
    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)',
    border: '1px solid #eee',
    height: '150px',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center'
  },
  newsLink: {
    textDecoration: 'none',
    color: 'inherit'
  },
  newsTitle: {
    fontSize: '1.1rem',
    fontWeight: 600,
    marginBottom: '0.5rem',
    display: '-webkit-box',
    WebkitLineClamp: 3,
    WebkitBoxOrient: 'vertical',
    overflow: 'hidden'
  },
  newsTime: {
    fontSize: '0.9rem',
    color: '#666'
  },
  navButton: {
    position: 'absolute',
    top: '50%',
    transform: 'translateY(-50%)',
    background: 'white',
    border: '1px solid #eee',
    borderRadius: '50%',
    width: '40px',
    height: '40px',
    cursor: 'pointer',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '1.2rem'
  },
  prevButton: {
    left: 0
  },
  nextButton: {
    right: 0
  },
  pagination: {
    display: 'flex',
    justifyContent: 'center',
    gap: '8px',
    marginTop: '1.5rem',
    marginBottom: '1.5rem',
  },
  paginationDot: {
    width: '8px',
    height: '8px',
    borderRadius: '50%',
    backgroundColor: '#ddd',
    border: 'none',
    padding: 0,
    cursor: 'pointer',
    transition: 'all 0.3s ease'
  },
  activeDot: {
    backgroundColor: '#333',
    width: '16px',
    borderRadius: '4px'
  }
};

const parseTimeString = (timeString) => {
  const now = new Date();
  const regexRelative = /^(\d+) (days?|hours?|minutes?) ago$/;
  const regexAbsolute = /^(\d{1,2}) ([A-Za-z]{3})$/;

  // Check for relative time strings
  const matchRelative = timeString.match(regexRelative);
  if (matchRelative) {
    const value = parseInt(matchRelative[1], 10);
    const unit = matchRelative[2];
    switch (unit) {
      case 'day':
      case 'days':
        return new Date(now.getTime() - value * 24 * 60 * 60 * 1000);
      case 'hour':
      case 'hours':
        return new Date(now.getTime() - value * 60 * 60 * 1000);
      case 'minute':
      case 'minutes':
        return new Date(now.getTime() - value * 60 * 1000);
    }
  }

  // Check for specific date strings
  const matchAbsolute = timeString.match(regexAbsolute);
  if (matchAbsolute) {
    const day = parseInt(matchAbsolute[1], 10);
    const month = new Date(Date.parse(matchAbsolute[2] + " 1, 2022")).getMonth(); // Using a dummy year
    return new Date(now.getFullYear(), month, day);
  }

  return null; // Return null if parsing fails
};

const GoogleNews = ({ data }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [timeFilter, setTimeFilter] = useState('latest');
  const itemsPerPage = 3;

  useEffect(() => {
    setCurrentIndex(0);
  }, [timeFilter]);

  const filteredData = useMemo(() => {
    if (!Array.isArray(data)) return [];

    const currentDate = new Date();

    return data.filter(item => {
      const parsedTime = parseTimeString(item.time);

      if (!parsedTime) return false; // Skip if parsing fails

      switch (timeFilter) {
        case 'latest':
          // Show all news with relative timestamps
          return item.time.includes('ago');

        case 'this-month':
          return parsedTime.getMonth() === currentDate.getMonth() && 
                 parsedTime.getFullYear() === currentDate.getFullYear();

        case '6-months': {
          const sixMonthsAgo = new Date();
          sixMonthsAgo.setMonth(currentDate.getMonth() - 6);
          return parsedTime >= sixMonthsAgo;
        }

        case 'this-year':
          return parsedTime.getFullYear() === currentDate.getFullYear();

        default:
          return false;
      }
    });
  }, [data, timeFilter]);

  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  const nextSlide = () => {
    setCurrentIndex((prev) => 
      prev + itemsPerPage >= filteredData.length ? 0 : prev + itemsPerPage
    );
  };

  const prevSlide = () => {
    setCurrentIndex((prev) => 
      prev - itemsPerPage < 0 ? 
        Math.max(0, filteredData.length - itemsPerPage) : 
        prev - itemsPerPage
    );
  };

  const goToPage = (pageIndex) => {
    setCurrentIndex(pageIndex * itemsPerPage);
  };

  const visibleItems = filteredData.slice(
    currentIndex,
    currentIndex + itemsPerPage
  );

  // Early return for no data
  if (filteredData.length === 0) {
    return (
      <div style={styles.googleNews}>
        <div style={styles.headerContainer}>
          <h2 style={styles.title}>Google News</h2>
          <select 
            value={timeFilter}
            onChange={(e) => setTimeFilter(e.target.value)}
            style={styles.timeFilter}
          >
            <option value="latest">Latest</option>
            <option value="this-month">This Month</option>
            <option value="6-months">Last 6 Months</option>
            <option value="this-year">This Year</option>
          </select>
        </div>
        <div>No news available for the selected time period.</div>
      </div>
    );
  }

  return (
    <div style={styles.googleNews}>
      <div style={styles.headerContainer}>
        <h2 style={styles.title}>Google News</h2>
        <select 
          value={timeFilter}
          onChange={(e) => setTimeFilter(e.target.value)}
          style={styles.timeFilter}
        >
          <option value="latest">Latest</option>
          <option value="this-month">This Month</option>
          <option value="6-months">Last 6 Months</option>
          <option value="this-year">This Year</option>
        </select>
      </div>

      <div style={styles.carouselContainer}>
        <button
          onClick={prevSlide}
          style={{...styles.navButton, ...styles.prevButton}}
          aria-label="Previous slide"
        >
          ←
        </button>

        <div style={styles.newsContainer}>
          {visibleItems.map((newsItem, index) => (
            <div key={currentIndex + index} style={styles.newsTile}>
              <a href={newsItem.link} target="_blank" rel="noopener noreferrer" style={styles.newsLink}>
                <h3 style={styles.newsTitle}>{newsItem.title}</h3>
                <p style={styles.newsTime}>{newsItem.time}</p>
              </a>
            </div>
          ))}
        </div>

        <button
          onClick={nextSlide}
          style={{...styles.navButton, ...styles.nextButton}}
          aria-label="Next slide"
        >
          →
        </button>
      </div>

      <div style={styles.pagination}>
        {Array.from({ length: totalPages }).map((_, idx) => (
          <button
            key={idx}
            onClick={() => goToPage(idx)}
            style={{
              ...styles.paginationDot,
              ...(Math.floor(currentIndex / itemsPerPage) === idx ? styles.activeDot : {})
            }}
            aria-label={`Go to page ${idx + 1}`}
          />
        ))}
      </div>
    </div>
  );
};

export default GoogleNews;