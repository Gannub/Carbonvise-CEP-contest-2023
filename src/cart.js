import './cart.css'
import minusCart from './images/market-inside/bx-minus.png';
import plusCart from './images/market-inside/bx-plus.png';
import mastercardLogo from './images/cart/Mastercard.jpg';
import applePay from './images/cart/ApplePay.jpg';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';

const Cart = () => {
    return ( 
        <div className="container">
            <div className="cart-block">
                <div className="cart-block-container">
                    {/* <div className="table-handmade">
                        <div className="nav-table">
                            <div className="table-description">Description</div>
                            <div className="table-qty">QTY</div>
                            <div className="table-chestnuts">Chestnuts</div>
                        </div>
                        <div className="underline-cart"></div>
                        <div className="content-table">
                            <div className='description-content'>
                                <div className="description-content-main">
                                    Embrace Solar Power
                                </div>
                                <div className="description-content-category">
                                    Solar energy
                                </div>
                            </div>
                            <div className='adjust-num-cart'>
                                <div className="minus-cart">
                                    <img src={minusCart} alt="" />
                                </div>
                                <div className="num-cart">4</div>
                                <div className="plus-cart">
                                    <img src={plusCart} alt="" />
                                </div>
                            </div>
                            <div className='chestnuts-cart'>
                                11,612
                            </div>
                        </div>
                        <div className="content-table">
                            <div className='description-content'>
                                <div className="description-content-main">
                                    Home hydropower
                                </div>
                                <div className="description-content-category">
                                    Waste Heat Recovery
                                </div>
                            </div>
                            <div className='adjust-num-cart'>
                                <div className="minus-cart">
                                    <img src={minusCart} alt="" />
                                </div>
                                <div className="num-cart">1</div>
                                <div className="plus-cart">
                                    <img src={plusCart} alt="" />
                                </div>
                            </div>
                            <div className='chestnuts-cart'>
                                2,903
                            </div>
                        </div>
                        <div className="content-table">
                            <div className='description-content'>
                                <div className="description-content-main">
                                    EcoPower
                                </div>
                                <div className="description-content-category">
                                    Renewable energy
                                </div>
                            </div>
                            <div className='adjust-num-cart'>
                                <div className="minus-cart">
                                    <img src={minusCart} alt="" />
                                </div>
                                <div className="num-cart">1</div>
                                <div className="plus-cart">
                                    <img src={plusCart} alt="" />
                                </div>
                            </div>
                            <div className='chestnuts-cart'>
                                903
                            </div>
                        </div>
                    </div> */}

                    <table className="cart-table">
                        <thead>
                            <tr>
                                <th>Description</th>
                                <th>QTY</th>
                                <th>Chestnuts</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    Embrace Solar Power
                                    </div>
                                    <div className="description-content-category">
                                    Solar energy
                                    </div>
                                </td>
                                <td className='adjust-num-cart'>
                                    <div className="minus-cart">
                                        <img src={minusCart} alt="" />
                                    </div>
                                    <div className="num-cart">4</div>
                                    <div className="plus-cart">
                                        <img src={plusCart} alt="" />
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    11,612
                                </td>
                            </tr>
                            <tr>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    Home hydropower
                                    </div>
                                    <div className="description-content-category">
                                    Waste Heat Recovery
                                    </div>
                                </td>
                                <td className='adjust-num-cart'>
                                    <div className="minus-cart">
                                        <img src={minusCart} alt="" />
                                    </div>
                                    <div className="num-cart">1</div>
                                    <div className="plus-cart">
                                        <img src={plusCart} alt="" />
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    2,903
                                </td>
                            </tr>
                            <tr>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    EcoPower
                                    </div>
                                    <div className="description-content-category">
                                    Renewable energy
                                    </div>
                                </td>
                                <td className='adjust-num-cart'>
                                    <div className="minus-cart">
                                        <img src={minusCart} alt="" />
                                    </div>
                                    <div className="num-cart">1</div>
                                    <div className="plus-cart">
                                        <img src={plusCart} alt="" />
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    903
                                </td>
                            </tr>
                        </tbody>
                    </table>

                    <div className="payment-title">
                        Payment methods
                    </div>
                    <div className="underline-cart"></div>
                    <div className="wrapper">
                    <div className="payment-cart">
                        <div className="payment-cart-nav">
                            <div className="payment-cart-name">Mastercard</div>
                            <div className="payment-cart-logo"><img src={mastercardLogo} alt="" /></div>
                        </div>
                        <div className="payment-cart-block">
                            <div className="payment-cart-block-container">
                            <div className="payment-username">Lucille de Chestnuts</div>
                            <div className="payment-id">**** **** **** 4321</div>
                            <div className="payment-date-default">
                                <div className="payment-date">XX/20XX</div>
                                <div className="payment-default">Default</div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div className="payment-cart">
                        <div className="payment-cart-nav">
                            <div className="payment-cart-name">Mastercard</div>
                            <div className="payment-cart-logo"><img src={applePay} alt="" /></div>
                        </div>
                        <div className="payment-cart-block">
                            <div className="payment-cart-block-container">
                            <div className="payment-username">Lucille de Chestnuts</div>
                            <div className="payment-id">**** **** **** 4321</div>
                            <div className="payment-date-default">
                                <div className="payment-date">XX/20XX</div>
                                <div className="payment-default">Default</div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div className="payment-cart-plus">
                        <div className="payment-cart-nav">
                            <div className="payment-cart-name-add">Add more methods</div>
                            <div className="payment-cart-logo"></div>
                        </div>

                        {/* center!!(not good code) */}

                        <div className="payment-cart-block-plus">
                            <div className="payment-cart-block-container-plus">
                                <div className="payment-plus">
                                    <Link to="">+</Link>
                                </div>
                            </div>
                        </div>
                    </div>
                    </div>
                    <div className="vat">VAT : 7%</div>
                    <div className="chestnuts-total">
                        <div className="chestnuts-total-text">TOTAL (Chestnuts) :</div>
                        <div className="chestnuts-total-amount">15,418</div>
                    </div>
                    <div className="underline-cart"></div>
                    <Link to="/receipt">
                    <button className="checkout-btn">
                        Checkout
                    </button>
                    </Link>
                </div>
            </div>
        </div>
     );
}
export default Cart;