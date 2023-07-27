import React,{useState, useEffect} from 'react'

import React from 'react'

const api = () => {
    let [infos, setInfos] = useState([])

    useEffect(() => {
        getInfos()
    }, [])
    
    let getInfos = async() => {
        let response =  await fetch("/api/")
        let data = await response.json()
        console.log('DATA:',data)
        setInfos(data)
    }

    return (
        <div>
            <div className='infos-list'>
                {infos.map((info, index)=>
                    <h3 key = {index}>{info.first_name}</h3>
                )}
            </div>
        </div>
    )
}

export default api