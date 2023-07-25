import './footer.css'
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

const Footer = () => {
    return ( 
        <div className="container">
        <footer>
            <div className="wrapper-foot">
                <div className="help">
                    <Link to="">Help Center</Link>
                </div>
                <div className="contact">
                    <Link to="">Contact Us</Link>
                </div>
                <div className="jobs">
                    <Link to="">Jobs</Link>
                </div>
                <br />
            </div>
            <div className="wrapper-foot">
                <div className="term">
                    <Link to="">Terms of Use</Link>
                </div>
                <div className="privacy">
                    <Link to="">Privacy Policy</Link>
                </div>
                <div className="cookie">
                    <Link to="">Cookie Preferences</Link>
                </div>
                <br />
            </div>
            <div className="wrapper-foot">
                <div className="last"> © 2023  Carbonvise Inc. All rights reserved.</div>
            </div>
        </footer>
        </div>
     );
}
 
export default Footer;