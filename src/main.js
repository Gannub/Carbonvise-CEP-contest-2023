import './main.css'
import {Link} from 'react-router-dom';
import arrowBlack from './images/main/bx-link-external 2.jpg';

const  MainPage= () => {
    return (  
        <div className="container">
            <div className="top-main-page">

            </div>
            <div className="mid-main-page">
                <div className="wrapper">
                    <div className="mid-main-page-leftText">
                    <div className="mid-main-page-leftText-container">
                                Inadequate disposal of plastic waste is the main driver of global plastic leakage, but microplastics, littering and losses from marine activities are also key concerns
                            Plastic pollution has now been documented in all the major ocean basins, beaches, rivers, lakes, terrestrial environments and even in remote locations such as the Arctic and Antarctic. Estimated global leakage to the environment (terrestrial and aquatic) was 22 Mt in 2019. This value is projected to double, reaching 44 Mt by 2060.
                            The vast majority are macroplastics, recognisable items such as beverage bottles, and most found their way into the natural environment as a result of inadequate collection and disposal. Other leakage routes include littering or fly-tipping, and marine activities. Microplastics, small pieces of plastic, less than 5 mm (0.2 inch) in length, also make up a sizeable share of total leakage, largely reaching the environment through wear to tyres and road markings, as well as the accidental loss of plastic pellets and washing of synthetic textile fibres.
                            These numbers stress the urgency of addressing waste management practices, while taking into account littering, leakage from marine activities and the steadily increasing microplastics leakage around the world.
                        <div className="mid-main-page-underline"></div>
                        <div className="plastic-bag-description">
                            <div className="plastic-bag-description-title">
                                <div className="plastic-bag-text">Plastic bag</div>
                                <div className="underline-plastic"></div>
                            </div>
                            <div className="plastic-bag-description-content">
                            have a global warming potential ranging from 1.7 to 3.5 kg of CO2 emissions, it is crucial to establish carbon credits to incentivize the adoption of more environmentally friendly alternatives.
                            </div>
                        </div>
                    </div>
                    </div>
                    <div className="mid-main-page-sectionLine"></div>
                    <div className="mid-main-page-rightPic"></div>
                </div>
            </div>
            <div className="bottom-main-page">
                <div className="bottom-main-page-container">
                    <div className="bottom-main-page-nav">
                        <div className="year-title">2022</div>
                        <div className="connect-line"></div>
                        <div className="purpose-title">The purpose <br /> of our website</div>
                        <div className="connect-line"></div>
                        <div className="mission-title">Our mission in 2023</div>
                    </div>
                    <div className="bottom-main-page-content">
                        <div className="year-title-content">
                            <div className="issued">Issued</div>
                            <div className="issued-number">1,559,805,845</div>
                            <div className="retired">Retired</div>
                            <div className="retired-number">830,551,199</div>
                            <div className="non-retired">Non-Retired</div>
                            <div className="non-retired-number">729,254,646</div>
                            <div className="volume-in-tCO2e">Volume in tCO2e <Link to="/"><img src={arrowBlack} alt="" /></Link></div>
                        </div>
                        <div className="purpose-title-content">
                            <div className="purpose-title-content-container">
                                <div className="purpose-title-content-text">is to promote awareness and engagement in the Carbon Credit project, empowering individuals and businesses to offset their carbon footprint, particularly by addressing the environmental impact of plastic bags, and fostering a sustainable future for our planet.</div>
                                <Link to="/"><img src={arrowBlack} alt="" /></Link>
                            </div>
                        </div>
                        <div className="mission-title-content">
                            <div className="vertical-line"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
 
export default MainPage;