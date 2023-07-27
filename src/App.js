import Navbar from './navbar';
import Profile from './profile';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Market from './market';
import Blogs from './blogs';
import Leaderboard from './leaderboard';
import Cart from './cart';
import Signin from './signin';
import MarketInside from './market-inside.js';
import BlogsInside from './blogs-inside';
import Receipt from './receipt';
import MainPage from './main';

function App() {
  return (
    <Router>
    <div className="App">
      <Navbar></Navbar>
        <Switch>
        <Route exact path="/">
        <MainPage></MainPage>
          </Route>
        <Route path="/market">
            <Market></Market>
          </Route>
          <Route path="/blogs">
            <Blogs></Blogs>
          </Route>
          <Route path="/leaderboard">
            <Leaderboard></Leaderboard>
          </Route>
          <Route path="/profile">
            <Profile></Profile>
          </Route>
          <Route path="/cart">
            <Cart></Cart>
          </Route>
          <Route path="/sign-in">
            <Signin></Signin>
          </Route>
          <Route path="/market-inside">
            <MarketInside></MarketInside>
          </Route>
          <Route path="/blogs-inside">
            <BlogsInside></BlogsInside>
          </Route>
          <Route path="/receipt">
            <Receipt></Receipt>
          </Route>
        </Switch>
    </div>
    </Router>
  );
}
export default App;

//First Page
