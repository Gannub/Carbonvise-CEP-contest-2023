import {Link} from 'react-router-dom';
import USERFACE from './images/profile/userface.jpg';
import arrow from './images/profile/bx-link-external 1.jpg';
import leaf from './images/market-inside/leaf.jpg';
import threeDot from './images/market-inside/bx-dots-horizontal-rounded 1.jpg'
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
            <div className="side-profile">
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
                    <div className="follow-btn"><Link to="/profile">Follow</Link></div>
                </div>
                <div className="wrapper-profile">
                    <div className="rank-andmore-block">
                        <div className="rank-block">
                        <div className="rank-block-container">
                            <div className="rank-text">Rank</div>
                            <div className="number-order">#20</div>
                            <div className="streak">4 week streak</div>
                        </div>
                        </div>
                        <div className="andmore-block">
                            and more...
                        </div>
                    </div>
                    <div className="reduced-block">
                        <div className="reduced-block-container">
                            <div className="reduced-text">Reduced</div>
                            <div className="percent">34%</div>
                            <div className="from-text">from</div>
                            <div className="chestnuts-amount">2,4453,867 Chestnuts </div>
                        </div>
                    </div>
                    <div className="carbon-status-block">
                        <div className="carbon-status-block-container">
                            <div className="carbon-text">Carbon</div>
                            <div className="offset-natural">Offsets</div>
                        </div>
                    </div>
                </div>
                <div className="project">
                    <div className="project-container">
                        <div className="project-title">Projects</div>
                        <div className="project-content">
                        <div className="wrapper-project">
                    <Link to="/market-inside">
                    <div className="product1-profile">
                        <div className="related-pic-1-profile">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Renewable energy</Link>
                            </div>
                        </div>
                        <div className="about-pic-profile">
                            <div className="about-pic-left">
                                <div className="type-profile">EcoPower</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    5.0(52 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num-profile">324</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    </Link>
                    <div className="product2-profile">
                        <div className="related-pic-2-profile">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Solar energy</Link>
                            </div>
                        </div>
                        <div className="about-pic-profile">
                            <div className="about-pic-left">
                                <div className="type-profile">Embrace Solar Power</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    4.9(39 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num-profile">500</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    <div className="product3-profile">
                        <div className="related-pic-3-profile">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Waste Heat Recovery</Link>
                            </div>
                        </div>
                        <div className="about-pic-profile">
                            <div className="about-pic-left">
                                <div className="type-profile">Embrace Solar Power</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    1.9(70 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num-profile">2903</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    </div>
                        </div>
                    </div>
                </div>
                <div className="blogs-profile">
                    <div className="blogs-profile-container">
                        <div className="blogs-text">Blogs</div>
                        <div className="blogs-content">
                        <div className="secondblog-profile">
                        <div className="container-eachblog-profile">
                        <div className="nav-eachblog-profile">
                            <div className="time-profile">16 hour ago</div>
                            <div className="three-dot"><img src={threeDot} alt="" /></div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Revitalize Your Morning Routine...</div>
                            <div className="text-blog">Start your day off right with these refreshing and nutritious vegan 
                            smoothie recipes. Packed with vitamins, minerals, and plant-based protein</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/events">Events</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div className="thirdblog-profile">
                        <div className="container-eachblog-profile">
                        <div className="nav-eachblog-profile">
                            <div className="time-profile">18 hour ago</div>
                            <div className="three-dot"><img src={threeDot} alt="" /></div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Mastering the Art of Communication</div>
                            <div className="text-blog">Enhance your communication skills by understanding different 
                            communication styles, active listening techniques, and fostering effective dialogue</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/events">Events</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default Profile;