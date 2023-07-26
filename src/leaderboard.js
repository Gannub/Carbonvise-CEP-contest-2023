import './leaderboard.css'
import { Link } from 'react-router-dom/cjs/react-router-dom';

const Leaderboard = () => {

    const changeCategory = event => {
        if (event.currentTarget.className === 'subcategory') {
            event.currentTarget.classList.toggle('subcategory-selected');
        }
    }
    return ( 
        <div className="container">
            <div className="top-block">
            <div className="top-block-container">
                <div className="blog-title">
                    <h1>Leaderboard</h1>
                </div>
                <div className="filter-search-sorted-wrapper">
                    <div className="filter-test">
                        <div className="layerst">
                            <div className="filter-blogs">filter </div>
                            <div className="underline-filter-leaderboard"></div>
                        </div>
                        <div className="category-blog">
                            <Link to="/leaderboard/today">
                            <div className="subcategory-selected " onClick={changeCategory}>
                                Today
                            </div>
                            </Link>
                            <Link to="/leaderboard/week"  >
                            <div className="subcategory" onClick={changeCategory}>
                                Week
                            </div>
                            </Link>
                            <Link to="/leaderboard/month">
                            <div className="subcategory" onClick={changeCategory}>
                                Month
                            </div>
                            </Link>
                            <Link to="/leaderboard/all-time">
                            <div className="subcategory" onClick={changeCategory}>
                                All time
                            </div>
                            </Link>
                        </div>
                    </div>
                    <div className="sorted-test">
                        <div className="layerst">
                            <div className="sorted-blog">Last update</div>
                            <div className="underLine-last-update"></div>
                        </div>
                        <div className="Last-update-date">
                            July 21, 2023, 2:18 a.m.
                        </div>
                    </div>
                </div>
            </div>
            </div>
            <div className="table-block">
                <div className="table-block-container">
                    <table className="leaderboard-table">
                        <thead>
                            <tr>
                                <th>Rank</th>
                                <th>Province</th>
                                <th>Majorities</th>
                                <th>Neutral Users</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>1</td>
                                <td>Bangkok</td>
                                <td className="offset">Offsets</td>
                                <td>23,434,543</td>
                            </tr>
                            <tr>
                                <td>2</td>
                                <td>Chiang Mai</td>
                                <td className="neutral">Neutral</td>
                                <td>20,494,757</td>
                            </tr>
                            <tr>
                                <td>3</td>
                                <td>Phuket</td>
                                <td className="neutral">Neutral</td>
                                <td>10,765,543</td>
                            </tr>
                            <tr>
                                <td>4</td>
                                <td>Chiang Rai</td>
                                <td className="neutral">Neutral</td>
                                <td>10,086,879</td>
                            </tr>
                            <tr>
                                <td>5</td>
                                <td>Rayong</td>
                                <td className="neutral">Neutral</td>
                                <td>10,004,543</td>
                            </tr>
                            <tr>
                                <td>6</td>
                                <td>Royuela de Rio Franco</td>
                                <td className="neutral">Neutral</td>
                                <td>9,786,786</td>
                            </tr>
                            <tr>
                                <td>7</td>
                                <td>La Descubierta</td>
                                <td className="offset">Offsets</td>
                                <td>9,435,756</td>
                            </tr>
                            <tr>
                                <td>8</td>
                                <td>Tegalsari</td>
                                <td className="offset">Offsets</td>
                                <td>9,345,543</td>
                            </tr>
                            <tr>
                                <td>9</td>
                                <td>Galunggalung</td>
                                <td className="neutral">Neutral</td>
                                <td>8,547,543</td>
                            </tr>
                            <tr>
                                <td>10</td>
                                <td>La Tour-du-Crieu</td>
                                <td className="neutral">Neutral</td>
                                <td>43,543</td>
                            </tr>
                            <tr>
                                <td>11</td>
                                <td>Kapakabisa</td>
                                <td className="neutral">Neutral</td>
                                <td>34,543</td>
                            </tr>
                            <tr>
                                <td>12</td>
                                <td>Wage Cibahayu</td>
                                <td className="neutral">Neutral</td>
                                <td>23,543</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
     );
}
export default Leaderboard;

