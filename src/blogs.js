import './blogs.css'
import Footer from "./footer";
import { Link } from 'react-router-dom/cjs/react-router-dom.min';
import dropdown from './images/blogs/dropdown.jpg';
import userBlog1 from './images/blogs/userpicblog1.png'
import userBlog2 from './images/blogs/userpicblog2.png'
import userBlog3 from './images/blogs/userpicblog3.png'
import userBlog4 from './images/blogs/userpicblog4.png'
import userBlog5 from './images/blogs/userpicblog5.png'
import userBlog6 from './images/blogs/userpicblog6.png'
import userBlog7 from './images/blogs/userpicblog7.png'

const Blogs = () => {
    return ( 
        <div className="container">
            <div className="top-block">
            <div className="top-block-container">
                <div className="blog-title">
                    <h1>Blogs</h1>
                </div>
                <div className="filter-search-sorted-wrapper">
                    <div className="filter-test">
                        <div className="layerst">
                            <div className="filter-blogs">filter </div>
                            <div className="underLine-filter"></div>
                        </div>
                        <div className="category-blog">
                            <div className="subcategory-selected">
                                <Link to="/blogs/foryou">For you</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/blogs/tips">Tips</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/blogs/news">News</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/blogs/events">Events</Link>
                            </div>
                        </div>
                    </div>
                    <div className="search-test">
                        <div className="layerst">
                            <div className="search">search</div>
                            <div className="underLine-search"></div>
                        </div>
                        <div className="search-box">
                            <form action="/action_page.php">
                            <input type="text" placeholder="Search.." name="search"/>
                            <button type="submit"><i className="fa fa-search"></i></button>
                            </form>
                        </div>
                    </div>
                    <div className="sorted-test">
                        <div className="layerst">
                            <div className="sorted-blog">sorted by</div>
                            <div className="underLine-sorted"></div>
                        </div>
                        <div className="Tdropdown">
                            <div className="drop-date">
                                <div className="date-text">date</div>
                                <div className="dropdown-btn"><img src={dropdown} alt="" /></div>
                            </div>
                            <div className="drop-views">
                                <div className="views-text">views</div>
                                <div className="dropdown-btn"><img src={dropdown} alt="" /></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div className="all-blogs">
                <div className="wrapper-blogs">
                    <Link to="/blogs-inside">
                    <div className="firstblog">
                        <div className="nav-blog1">
                            <div className="userBlog">
                                <img src={userBlog1} alt="" />
                            </div>
                            <div className="username-blogs">Elementum eleifend</div>
                            <div className="time">1 hour ago</div>
                        </div>
                        <div className="underline-navblog"></div>
                        <div className="below-blog1">
                            <div className="title-blog">
                                The Art of Productivity: Effective Strategies for Getting Things Done
                            </div>
                            <div className="text-blog">Discover the ultimate guilt-free pleasure with these mouthwatering vegan 
                            chocolate chip cookies. They are soft, chewy, and loaded with chocolatey goodness. Get ready to 
                            impress your friends and family with this delightful recipe that proves vegan desserts can be 
                            just as satisfying.</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                    </div>
                    </Link>
                    <div className="secondblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog2} alt="" />
                            </div>
                            <div className="username-blogs">Sollicitudin</div>
                            <div className="time">16 hour ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Revitalize Your Morning Routine...</div>
                            <div className="text-blog">Start your day off right with these refreshing and nutritious vegan 
                            smoothie recipes. Packed with vitamins, minerals, and plant-based protein</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div className="thirdblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog3} alt="" />
                            </div>
                            <div className="username-blogs">Curabitur</div>
                            <div className="time">18 hour ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Mastering the Art of Communication</div>
                            <div className="text-blog">Enhance your communication skills by understanding different 
                            communication styles, active listening techniques, and fostering effective dialogue</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                </div>
                <div className="wrapper-blogs-under">
                    <div className="fourthblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog4} alt="" />
                            </div>
                            <div className="username-blogs">Etiam</div>
                            <div className="time">20 hour ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Unlocking Creativity: Igniting Your ...</div>
                            <div className="text-blog">Explore methods to tap into your creativity, 
                            overcome creative blocks, and foster a more innovative mindset.</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div className="fifthblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog5} alt="" />
                            </div>
                            <div className="username-blogs">Donec</div>
                            <div className="time">21 hour ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">Navigating Change: Embracing ...</div>
                            <div className="text-blog">Learn strategies to adapt to change, embrace uncertainty, 
                            and harness new opportunities for personal and professional growth.</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div>
                        </div>
                    </div>
                    <div className="sixthblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog6} alt="" />
                            </div>
                            <div className="username-blogs">Aliquam</div>
                            <div className="time">1 day ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">The Power of Positive Thinking</div>
                            <div className="text-blog">Discover the influence of positive thinking on your overall 
                            well-being and explore techniques to cultivate a positive mindset.</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
                                </div>
                                <div className="read-more">
                                    <Link to="/blogs/read-more">Read more</Link>
                                </div>
                            </div>
                        </div> 
                        </div>
                    </div>
                    <div className="seventhblog">
                        <div className="container-eachblog">
                        <div className="nav-eachblog">
                            <div className="userBlog">
                                <img src={userBlog7} alt="" />
                            </div>
                            <div className="username-blogs">Interdum</div>
                            <div className="time">1 week ago</div>
                        </div>
                        <div className="underline-eachblog"></div>
                        <div className="below-eachblog">
                            <div className="title-blog">The Art of Decision Making: Strategies ...</div>
                            <div className="text-blog">Gain insights into decision-making processes, learn how to overcome 
                            decisio paralysis, and make more informed and effective choices.</div>
                            <div className="tips-readmore">
                                <div className="tips"> 
                                    <Link to="/blogs/tips">Tips</Link>
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
            <Footer></Footer>
        </div>
     );
}
export default Blogs;