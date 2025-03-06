// src/theme.js - Theme configuration
import { createGlobalStyle } from 'styled-components';

// Theme colors and values
export const theme = {
  colors: {
    primary: '#1a1a24',
    secondary: '#2e2e36',
    accent: '#6358dc',
    accentHover: '#4a41c8',
    text: '#ffffff',
    textSecondary: '#b3b3b3',
    success: '#4CAF50',
    error: '#f44336',
    warning: '#ff9800',
    info: '#2196F3',
    cardBg: '#27273a',
    border: '#3f3f56'
  },
  fonts: {
    body: "'Poppins', sans-serif",
    heading: "'Poppins', sans-serif"
  },
  fontSizes: {
    xs: '0.75rem',
    sm: '0.875rem',
    md: '1rem',
    lg: '1.125rem',
    xl: '1.25rem',
    '2xl': '1.5rem',
    '3xl': '1.875rem',
    '4xl': '2.25rem',
    '5xl': '3rem',
    '6xl': '3.75rem'
  },
  space: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
    xl: '2rem',
    '2xl': '3rem',
    '3xl': '4rem'
  },
  borders: {
    none: 'none',
    thin: '1px solid',
    normal: '2px solid',
    thick: '4px solid'
  },
  radii: {
    none: '0',
    sm: '0.125rem',
    md: '0.25rem',
    lg: '0.5rem',
    xl: '1rem',
    full: '9999px'
  },
  shadows: {
    sm: '0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24)',
    md: '0 4px 6px rgba(0, 0, 0, 0.12), 0 1px 3px rgba(0, 0, 0, 0.24)',
    lg: '0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23)',
    xl: '0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22)'
  },
  transitions: {
    fast: 'all 0.2s ease',
    normal: 'all 0.3s ease',
    slow: 'all 0.5s ease'
  },
  breakpoints: {
    sm: '576px',
    md: '768px',
    lg: '992px',
    xl: '1200px'
  }
};

// Global styles
export const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  html {
    font-size: 16px;
  }
  
  body {
    font-family: ${props => props.theme.fonts.body};
    background-color: ${props => props.theme.colors.primary};
    color: ${props => props.theme.colors.text};
    line-height: 1.5;
  }
  
  h1, h2, h3, h4, h5, h6 {
    font-family: ${props => props.theme.fonts.heading};
    margin-bottom: ${props => props.theme.space.md};
  }
  
  p {
    margin-bottom: ${props => props.theme.space.md};
  }
  
  a {
    color: ${props => props.theme.colors.accent};
    text-decoration: none;
    transition: ${props => props.theme.transitions.fast};
    
    &:hover {
      color: ${props => props.theme.colors.accentHover};
    }
  }
  
  button {
    cursor: pointer;
  }
  
  img {
    max-width: 100%;
  }
  
  .container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 ${props => props.theme.space.md};
  }
  
  .main-content {
    min-height: calc(100vh - 160px); /* Adjust based on navbar and footer height */
  }
`;