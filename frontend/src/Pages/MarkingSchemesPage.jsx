import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import MarkingSchemes from '../Components/MarkingSchemes/MarkingSchemes'
import {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'
function MarkingSchemesPage() {
  const { year,subjectId} = useParams()
  // console.log(year,subjectId)
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("outer");
  const [markingScheme,setMarkingScheme] = useState({});

  const name=`${subjectId}---- ${year} ---Marking Scheme`

  useEffect(()=>{
    console.log("DATA:");
    axios
    .get(`http://127.0.0.1:8000/api_v1/markings/${year}/${subjectId}`)
    .then((response) => {
      // const data = response.data
      // setMarkingScheme(response.data)
      // console.log("Marking scheme:",markingScheme.id)
      // Process the response data or update your React component state
    })
    .catch((error) => {
      console.error(error);
      // Handle the error, e.g., display an error message to the user
    });
  },[]);

  // //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    // console.log(isClicked)
    }else{
    setClick("outer")
    // console.log(isClicked)
    }
  }

  return (
    <div>
      <NavBar />
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <MarkingSchemes clicked={isClicked} data={markingScheme}/>
      
    </div>
  )
}

export default MarkingSchemesPage
