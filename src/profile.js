import {Link} from 'react-router-dom';
import USERFACE from './images/profile/userface.jpg';
import arrow from './images/profile/bx-link-external 1.jpg';
import forest from './images/profile/forest 1.jpg';
import './profile.css'

const Profile = () => {

    return ( 
        <div className="container">
            <div className="top-block-profile">
                <div className="top-block-profile-container">
                    <div className="profile-title">
                        <h1>Profile</h1>
                    </div>
                </div>
            </div>
            <div className="topside-profile">
                <div className="top-top-profile">
                    <div className="userFace">
                        <img src={USERFACE} alt="USERFACE" />
                    </div>
                    <div className="owner">
                        <div className="name">Samuel de Chestnuts </div> 
                        <div className="description">
                            description 
                            <Link to="/profile/description">
                            <img src={arrow} alt="ARROW" />
                            </Link>
                        </div>   
                    </div>
                </div>
                <div className="second-layer-profile">
                    <div className="wrapper">
                        <div className="balance-box">
                            Balance
                            <div className="number">2,445</div>
                            <div className="unit">Chestnuts </div>
                        </div>
                        <div className="rank-box">
                            Rank
                            <div className="number">#20</div>
                            <div className="unit">4 week streak </div>
                        </div>
                        <div className="favorite-box">
                            Favorite
                            <div className="describe">Reforestation</div>
                            <div className="wrapper-fav">
                                <div className="fav-pic">
                                    <img src={forest} alt="Forest-Pic" />
                                </div>
                                <div className="fav-number">245</div>
                            </div>
                            <div className="unit2">Chestnuts </div>
                        </div>
                        <div className="and-more-box">and more...</div>
                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default Profile;