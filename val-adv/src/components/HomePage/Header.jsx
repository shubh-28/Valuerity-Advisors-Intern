import React from 'react'
import './Header.css'

const Header = () => {
  return (
    <header className='header'>
        <a href="/" className='logo'>Logo</a>

        <nav className='navbar'>
            <a href="/">Home</a>
            <a href="/">About</a>
            <a href="/">Services</a>
            <a href="/">Contact</a>
        </nav>
    </header>
  )
}

export default Header