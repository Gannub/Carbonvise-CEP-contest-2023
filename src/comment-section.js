import './comment-section.css'
import emptyblackLeaf from './images/comment-section/emptyblackLeaf.jpg';
import FullblackLeaf from './images/comment-section/fullblackLeaf.jpg';
import userCommentPic1 from './images/comment-section/usercommentPic1.png'
import userCommentPic2 from './images/comment-section/usercommentPic2.png'
import emptyLeaf from './images/market-inside/leaf.jpg';
import FullLeaf from './images/market-inside/fullleaf.jpg';

const CommentSection = () => {
    return ( 
        <div className="container">
            <div className="comment-section">
                <div className="rating-comment">
                    <div className="num-comment"> 1.9 </div>
                    <div className="score">
                        <img src={FullblackLeaf} alt="" />
                        <img src={FullblackLeaf} alt="" />
                        <img src={emptyblackLeaf} alt="" />
                        <img src={emptyblackLeaf} alt="" />
                        <img src={emptyblackLeaf} alt="" />
                    </div>
                </div>
                <div className="all-comment">
                    <div className="user-comment">
                        <div className="userPic">
                            <img src={userCommentPic1} alt="" />
                        </div>
                        <div className="username-rating">
                            <div className="username-comment">Elementum eleifend</div>
                            <div className="score-small">
                                <img src={FullLeaf} alt="" />
                                <img src={FullLeaf} alt="" />
                                <img src={FullLeaf} alt="" />
                                <img src={FullLeaf} alt="" />
                                <img src={FullLeaf} alt="" />
                                <div className="mid-text">5.0</div>
                            </div>
                        </div>
                        <div className="comment">Aenean mattis mi tellus, sed blandit erat aliquet eget</div>
                        <div className="time">1 days ago</div>
                    </div>
                    <div className="user-comment">
                        <div className="userPic">
                            <img src={userCommentPic2} alt="" />
                        </div>
                        <div className="username-rating">
                            <div className="username-comment">Elementum eleifend</div>
                            <div className="score-small">
                                <img src={FullLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <div className="mid-text">1.1</div>
                            </div>
                        </div>
                        <div className="comment">Sed vitae elit lobortis, semper est ac, auctor turpis.</div>
                        <div className="time">13 weeks ago</div>
                    </div>
                </div>
            </div>
        </div>
     );
}
 
export default CommentSection;