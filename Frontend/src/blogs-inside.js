import './blogs-inside.css'
import userBlog1 from './images/blogs/userpicblog1.png'
import undo from './images/market-inside/bx-left-arrow-alt 1.png';
import dots from './images/market-inside/bx-dots-horizontal-rounded 1.jpg';
import userCommentPic1 from './images/comment-section/usercommentPic1.png'
import userCommentPic2 from './images/comment-section/usercommentPic2.png'
import { Link } from 'react-router-dom/cjs/react-router-dom.min';


const BlogsInside = () => {
    return ( 

        <div className="container">
            <div className="blogs-inside">
                <div className="blogs-insideContainer">
                    <div className="first-layer">
                        <div className="undo"><Link to="/blogs"><img src={undo} alt="" /></Link></div>
                        <div className="threedots"><img src={dots} alt="" /></div>
                    </div>
                    <div className="other-layer">
                    <div className="blogs-insideTitle">
                        The Art of Productivity: Effective Strategies for Getting Things Done
                    </div>
                    <div className="content-blogs">
                        <div className="firstlayer-blogs-inside">
                            <div className="userface-blogs"><img src={userBlog1} alt="" /></div>
                            <div className="username-blogs-inside">Elementum eleifend</div>
                            <div className="date-blogs">XX/XX/20XX</div>
                        </div>
                        <div className="secondlayer-blogs-inside">
                        In today's fast-paced world, where demands and distractions abound, mastering the art of productivity has become essential for achieving success and maintaining a sense of balance in our lives. Productivity is not merely about completing tasks; it's about accomplishing meaningful goals while optimizing our time, energy, and resources. Fortunately, there are several effective strategies that can help us enhance our productivity and make the most of our potential.

First and foremost, setting clear goals is crucial for productivity. By defining specific, measurable, achievable, relevant, and time-bound (SMART) goals, we provide ourselves with a roadmap to follow and a sense of direction. These goals act as our guiding stars, keeping us focused and motivated throughout our journey. Additionally, breaking down larger goals into smaller, manageable tasks enables us to approach them systematically, making progress more tangible and achievable.
Another key aspect of productivity is effective time management. Time is a finite resource, and how we allocate and utilize it greatly impacts our productivity. One powerful technique is prioritization. By identifying and prioritizing tasks based on their urgency and importance, we can ensure that we dedicate our time and energy to the most critical activities. Time blocking is another valuable strategy, involving the allocation of specific time slots for different tasks or activities. This practice helps eliminate multitasking and encourages deep focus and concentration, leading to increased efficiency.
                        </div>
                    </div>
                    <div className="comments-title">Comments</div>
                    <div className="underline-insideblogs"></div>

                        {/* responsive-comment */}
                        <div className="firstlayer-blogs-inside-res">
                            <div className="userface-blogs"><img src={userBlog1} alt="" /></div>
                            <div className="username-blogs-inside">Elementum eleifend</div>
                            <div className="date-blogs">XX/XX/20XX</div>
                        </div>
                    <div className="underline-insideblogs-res"></div>
                    <div className="comment-blogs-inside-res">
                        <div className="comment-title-res">Comments</div>
                        <div className="underline-comment-insideblogs-res"></div>
                    </div>
                    <div className="user-comment-res">
                        <div className="userPic">
                            <img src={userCommentPic1} alt="" />
                        </div>
                        <div className="otherthan-userpic">
                            <div className="username-date">
                                <div className="username-rating-res">
                                    <div className="username-comment-res">Elementum eleifend</div>
                                </div>
                                <div className="time">1 days ago</div>
                            </div>
                            <div className="comment-res">Aenean mattis mi tellus, sed blandit erat aliquet eget</div>
                        </div>
                    </div>
                    <div className="user-comment-res">
                        <div className="userPic">
                            <img src={userCommentPic2} alt="" />
                        </div>
                        <div className="otherthan-userpic">
                            <div className="username-date">
                                <div className="username-rating-res">
                                    <div className="username-comment-res">Sollicitudin nec sollicitudin</div>
                                </div>
                                <div className="time">13 weeks ago</div>
                            </div>
                            <div className="comment-res">Sed vitae elit lobortis, semper est ac, auctor turpis.</div>
                        </div>
                    </div>
                    {/* responsive-comment */}

                    <div className="comment-section-blogs">
                        <div className="all-comment-blogs">
                            <div className="user-comment">
                                <div className="userPic">
                                    <img src={userCommentPic1} alt="" />
                                </div>
                                <div className="username-rating">
                                    <div className="username-comment">Elementum eleifend</div>
                                </div>
                                <div className="comment">Aenean mattis mi tellus, sed blandit erat aliquet eget</div>
                                <div className="time">1 days ago</div>
                            </div>
                            <div className="user-comment">
                                <div className="userPic">
                                    <img src={userCommentPic2} alt="" />
                                </div>
                                <div className="username-rating">
                                    <div className="username-comment">Sollicitudin nec sollicitudin</div>
                                </div>
                                <div className="comment">Sed vitae elit lobortis, semper est ac, auctor turpis.</div>
                                <div className="time">13 weeks ago</div>
                            </div>
                        </div>
                    </div>
                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default BlogsInside;