import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { AuthProvider } from './context/AuthContext';
import { CartProvider } from './context/CartContext';

// Import layouts
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';

// Import pages
import Home from './pages/Home';
import ProductList from './pages/ProductList';
import ProductDetail from './pages/ProductDetail';
import Cart from './pages/Cart';
import Checkout from './pages/Checkout';
import Login from './pages/Login';
import Register from './pages/Register';
import UserProfile from './pages/UserProfile';
import AdminDashboard from './pages/AdminDashboard';
import NotFound from './pages/NotFound';

function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <CartProvider>
          <Router>
            <div className="app">
              <Navbar />
              <main className="main-content">
                <Switch>
                  <Route exact path="/" component={Home} />
                  <Route path="/products" component={ProductList} />
                  <Route path="/product/:id" component={ProductDetail} />
                  <Route path="/cart" component={Cart} />
                  <Route path="/checkout" component={Checkout} />
                  <Route path="/login" component={Login} />
                  <Route path="/register" component={Register} />
                  <Route path="/profile" component={UserProfile} />
                  <Route path="/admin/dashboard" component={AdminDashboard} />
                  <Route component={NotFound} />
                </Switch>
              </main>
              <Footer />
            </div>
          </Router>
        </CartProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;