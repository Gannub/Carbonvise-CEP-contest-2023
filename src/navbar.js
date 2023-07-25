import {Link} from 'react-router-dom';

const Navbar = () => {

    function showPopupMenu() {
        let popupMenu = document.getElementById('popupMenu');
        if (popupMenu.style.display === 'none') {
            popupMenu.style.display = 'block';
        } else{
            popupMenu.style.display = 'none';
        }
      }

    return ( 
        <div className="container">
            <nav>
                <ul>
                    <div className="logo">
                        <h1>LOGO</h1>
                        <div class="ham-menu" onClick={showPopupMenu}>
                            <div class="bar1"></div>
                            <div class="bar2"></div>
                            <div class="bar3"></div>
                        </div>
                        <div className="popup-menu" id='popupMenu'>
                            <li><Link to="/market">Market</Link></li>
                            <li><Link to="/blogs">Blogs</Link></li>
                            <li><Link to="/leaderboard">Leaderboard</Link></li>
                            <li><Link to="/profile">Samuel</Link></li>
                        </div>
                    </div>
                    <div className="wrapper">
                    <li><Link to="/market">Market</Link></li>
                    <li><Link to="/blogs">Blogs</Link></li>
                    <li><Link to="/leaderboard">Leaderboard</Link></li>
                    <li>
                            <div className="cart-logo">
                                <h1>Carbonvise</h1>
                            </div>
                    </li>
                    </div>
                    <div className="wrapper">
                        <li><Link to="/profile" className="username">Samuel</Link></li>
                        <li><Link to="/cart" className="cart">Cart</Link></li>
                    </div>
                </ul>
                <div className="under"></div>
            </nav>
        </div>
     );
}
export default Navbar;