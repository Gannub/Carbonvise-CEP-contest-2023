import './receipt.css'

const Receipt = () => {
    return ( 
        <div className="container">
            <div className="receipt-block">
                <div className="receipt-block-container">
                    <div className="carbonvise-title">Carbonvise Inc.</div>
                    <div className="order-id">Order #342</div>
                    <div className="date-receipt">Fri   23 / 06 / 2043   09:32:03 AM</div>
                    <table className="cart-table">
                        <thead>
                            <tr>
                                <th>QTY</th>
                                <th>Description</th>
                                <th>Chestnuts</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td className='adjust-num-cart'>
                                    <div className="num-cart">4</div>
                                </td>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    Embrace Solar Power
                                    </div>
                                    <div className="description-content-category">
                                    Solar energy
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    11,612
                                </td>
                            </tr>
                            <tr>
                                <td className='adjust-num-cart'>
                                    <div className="num-cart">1</div>
                                </td>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    Home hydropower
                                    </div>
                                    <div className="description-content-category">
                                    Waste Heat Recovery
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    2,903
                                </td>
                            </tr>
                            <tr>
                                <td className='adjust-num-cart'>
                                    <div className="num-cart">1</div>
                                </td>
                                <td className='description-content'>
                                    <div className="description-content-main">
                                    EcoPower
                                    </div>
                                    <div className="description-content-category">
                                    Renewable energy
                                    </div>
                                </td>
                                <td className='chestnuts-cart'>
                                    903
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div className="underline-cart"></div>
                    <div className="vat-receipt">VAT : 7%</div>
                    <div className="chestnuts-total">
                        <div className="chestnuts-total-text">TOTAL (Chestnuts) :</div>
                        <div className="chestnuts-total-amount">15,418</div>
                    </div>
                    <div className="underline-cart"></div>
                    <div className="card-type">
                        <div className="card-type-left">Card Type :</div>
                        <div className="card-type-right">Credit Card</div>
                    </div>
                    <div className="response">
                        <div className="response-left">Response :</div>
                        <div className="response-right">APPROVED</div>
                    </div>
                    <div className="approval-code">
                        <div className="approval-code-left">Approval Code :</div>
                        <div className="approval-code-right">893227</div>
                    </div>
                    <div className="thankYou">thank you for shopping with us</div>
                </div>
            </div>
        </div>
     );
}
 
export default Receipt;