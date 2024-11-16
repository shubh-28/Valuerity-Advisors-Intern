import React from 'react';
import Header from './Header';
import Main from './Main';

const HomePage = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <Main />
    </div>
  );
};

export default HomePage;
