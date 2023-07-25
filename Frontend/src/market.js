import './market.css'
import Footer from "./footer";
import { Link } from 'react-router-dom/cjs/react-router-dom.min';
import leaf from './images/market-inside/leaf.jpg';
import dropdown from './images/blogs/dropdown.jpg';

const Market = () => {
    return ( 
        <div className="container">
            <div className="top-block">
            <div className="top-block-container">
                <div className="market-title">
                    <h1>Market</h1>
                </div>
                <div className="filter-sorted-wrapper">
                    <div className="filter-section">
                        <div className="layerst">
                            <div className="filter">filter </div>
                            <div className="underLine"></div>
                        </div>
                        <div className="category">

                            <div className="wrapper-responsive-market">
                            <div className="subcategory-selected">
                                <Link to="/market/all">All</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/market/biomass">Biomass</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/market/biological">Biological</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/market/renewable energy">Renewable energy</Link>
                            </div>
                            </div>

                            <div className="wrapper-responsive-market-under">
                            <div className="subcategory-res">
                                <Link to="/market/hydropower">Hydropower</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/market/waste heat recovery">Waste Heat</Link>
                            </div>
                            <div className="subcategory">
                                <Link to="/market/solar energy">Solar energy</Link>
                            </div>
                            </div>

                        </div>
                    </div>
                    <div className="sorted-section">
                        <div className="layerst">
                            <div className="sorted">sorted by</div>
                            <div className="underLine2"></div>
                        </div>
                        <div className="Tdropdown">
                            <div className="drop-date">
                                <div className="date-text">date</div>
                                <div className="dropdown-btn"><img src={dropdown} alt="" /></div>
                            </div>
                            <div className="drop-price">
                                <div className="price-text">price</div>
                                <div className="dropdown-btn"><img src={dropdown} alt="" /></div>
                            </div>
                            <div className="drop-review">
                                <div className="review-text">review</div>
                                <div className="dropdown-btn"><img src={dropdown} alt="" /></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div className="product">
                <div className="wrapper-market">
                    <Link to="/market-inside">
                    <div className="product1">
                        <div className="related-pic-1">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Renewable energy</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">EcoPower</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    5.0(52 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">324</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    </Link>
                    <div className="product2">
                        <div className="related-pic-2">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Solar energy</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">Embrace Solar Power</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    4.9(39 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">500</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    <div className="product3">
                        <div className="related-pic-3">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Waste Heat Recovery</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">Embrace Solar Power</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    1.9(70 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">2903</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    <div className="product4">
                        <div className="related-pic-4">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Waste Heat Recovery</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">Waste Heat Recovery </div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    4.9(100 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">109</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="wrapper-market-under">
                    <div className="product5">
                        <div className="related-pic-5">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Hydropower</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">Home hydropower</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    3.9(10 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">309</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    <div className="product6">
                        <div className="related-pic-6">
                            <div className="subcategory-each">
                                <Link to="/market/renewable energy">Renewable energy</Link>
                            </div>
                        </div>
                        <div className="about-pic">
                            <div className="about-pic-left">
                                <div className="type">Home hydropower</div>
                                <div className="rating">
                                    <img src={leaf} alt="" />
                                    0.9(105 Reviews)
                                    </div>
                            </div>
                            <div className="about-pic-right">
                                <div className="num">909</div>
                                <div className="subunit">Chestnuts</div>
                            </div>
                        </div>
                    </div>
                    <div className="product7"></div>
                </div>
            </div>
            <Footer></Footer>
        </div>
     );
}
export default Market;