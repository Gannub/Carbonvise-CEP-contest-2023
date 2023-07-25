import './market-inside.css';
import undo from './images/market-inside/bx-left-arrow-alt 1.png';
import dots from './images/market-inside/bx-dots-horizontal-rounded 1.jpg';
import insidemarketpic from './images/market-inside/insideMarket.png';
import emptyLeaf from './images/market-inside/leaf.jpg';
import FullLeaf from './images/market-inside/fullleaf.jpg';
import { Link } from 'react-router-dom/cjs/react-router-dom';
import minus from './images/market-inside/bx-minus.png';
import plus from './images/market-inside/bx-plus.png';
import userpic from './images/market-inside/userpic.jpg'
import CommentSection from './comment-section';

const MarketInside = () => {
    return ( 
        <div className="container">
            <div className="market-inside">
            <div className="market-insideContainer">
                <div className="top-side">
                    <div className="first-layer">
                        <div className="undo"><Link to="/market"><img src={undo} alt="" /></Link></div>
                        <div className="threedots"><img src={dots} alt="" /></div>
                    </div>

                    <div className="second-layer">
                        <div className="left-second-layer">
                            <img src={insidemarketpic} alt="" />
                        </div>
                        <div className="mid-second-layer">
                            <div className="mid-title">Embrace Solar Power</div>
                            <div className="score"> 
                                <img src={FullLeaf} alt="" />
                                <img src={FullLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <img src={emptyLeaf} alt="" />
                                <div className="mid-text">1.9 ( 70 Reviews)</div>
                            </div>
                            <div className="mid-type">
                                <Link to="/market-inside/solar energy">Solar energy</Link>
                            </div>
                                <div className="mid-decription-title">Decription</div>
                                <div className="mid-decription-info">   Praesent tellus nunc, maximus id mi vel, consectetur tincidunt diam. Vivamus et urna magna. Donec efficitur, erat maximus lacinia sollicitudin, neque enim tincidunt tellus, 
                                quis porttitor metus velit in elit. Aenean a vulputate felis. Ut sit amet mattis dui, a pellentesque ex. Mauris lacus odio, tincidunt vitae turpis iaculis, pretium condimentum augue. Integer venenatis fringilla elit,
                                 a cursus arcu condimentum accumsan. Mauris dignissim vel massa id fermentum. Vivamus vestibulum libero vitae arcu faucibus feugiat. Sed mattis enim at arcu iaculis convallis. Nam vitae enim lobortis, vestibulum arcu quis,
                                  ultrices sapien. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
                                </div>
                        </div>
                        <div className="right-second-layer">
                            <div className="right-topbox">
                                <div className="upper-topbox">
                                    <div className="upper-topLeft">
                                        <div className="left-total">Total</div>
                                        <div className="adjust-num">
                                            <div className="minus"><img src={minus} alt="" /></div>
                                            <div className="x">01</div>
                                            <div className="plus"><img src={plus} alt="" /></div>
                                        </div>
                                    </div>
                                    <div className="upper-topRight">
                                        <div className="num">2903</div>
                                        <div className="subunit-inside">Chestnuts</div>
                                    </div>
                                </div>
                                <div className="upper-bottom">
                                    <div className="add-cart">
                                        <Link to="/market-inside/add-cart">add to cart</Link>
                                    </div>
                                    <div className="buy">
                                        <Link to="/market-inside/buy">buy</Link>
                                    </div>
                                </div>
                            </div>
                            <div className="right-botbox">
                                <div className="userpic">
                                    <img src={userpic} alt="" />
                                </div>
                                <div className="about-userpic">
                                    <div className="name-userpic">Aliquam commodo</div>
                                    <div className="wrapper">
                                        <div className="rating-userpic">3.9</div>
                                        <div className="view">
                                            <Link to="/market-inside/view">view</Link>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* responsive */}

                    <div className="second-layer-responsive">
                        <div className="mid-second-layer-res">
                            <div className="mid-title">Embrace Solar Power</div>
                            <div className="mid-img-market-inside-res">
                                
                            </div>
                            <div className="mid-decription-title">Decription</div>
                            <div className="mid-decription-info">   Lorem ipsum dolor sit amet consectetur adipisicing elit. In, similique! Corrupti iste quia repellendus deserunt officiis facere. Iusto quibusdam aperiam dolores aliquid itaque dolorum quis perferendis asperiores! Quibusdam, atque voluptatem!
                            </div>
                            <div className="underline-insideblogs-res"></div>
                            <div className="user-info-market-inside-res">
                                <div className="userpic-res">
                                    <img src={userpic} alt="" />
                                </div>
                                <div className="right-side-userpic">
                                    <div className="name-userpic">Aliquam commodo</div>
                                    <div className="rating-userpic">3.9</div>
                                    <div className="view">
                                        <Link to="/market-inside/view">view</Link>
                                    </div>
                                </div>
                            </div>
                            <div className="underline-insideblogs-res"></div>
                        </div>
                    </div>

                    {/* responsive */}
                </div>

                <div className="bot-side">
                    <div className="bot-sidenav">
                        <div className="RatingReviews">Rating & Reviews</div>
                        <div className="sorted">
                            <div className="uppersorted">
                                <div className="sorted-by">sorted by </div>
                                <div className="underline-sorted"></div>
                            </div>
                            <div className="lowersorted">
                                <div className="date">date</div>
                                <div className="reviews">reviews</div>
                            </div>
                        </div>
                    </div>
                    <div className="bot-underline"></div>
                    <div className="comment-section-component">
                    <CommentSection></CommentSection>
                    </div>
                </div>
            </div>
            </div>

            {/* added block-responsive  */}
            <div className="add-market-inside-res">
                <div className="add-market-inside-res-container">
                        <div className="left-side-added-block-res">
                            <div className="left-total">Total</div>
                            <div className="num">2903</div>
                            <div className="subunit-inside">Chestnuts</div>
                        </div>
                        <div className="right-side-added-block-res">
                            <div className="adjust-num">
                                <div className="minus"><img src={minus} alt="" /></div>
                                <div className="x">01</div>
                                <div className="plus"><img src={plus} alt="" /></div>
                            </div>
                            <div className="upper-bottom">
                                <div className="add-cart">
                                    <Link to="/market-inside/add-cart">add to cart</Link>
                                </div>
                                <div className="buy">
                                    <Link to="/market-inside/buy">buy</Link>
                                </div>
                            </div>
                        </div>
                </div>
            </div>
        </div>
     );
}
 
export default MarketInside;