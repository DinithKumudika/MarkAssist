import MarksBox from "./MarksBox"
import Button from "../Button"
import MarkAccurcyConfigure from "./MarkAccurcyConfigure"
import classnames from 'classnames';
import { useState , useEffect } from 'react'
import { MoonLoader } from 'react-spinners';
import Modal from "../Modal";
import axios from "axios";
import { useNavigate } from 'react-router-dom';
// import { set } from "mongoose";
function Marks({clicked,answers,markings}) {
  const navigate = useNavigate();
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const answersheets = JSON.parse(localStorage.getItem('answers'));
  // const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  // console.log(answers)
  // console.log(markings)
  const [showImages, setShowImages] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [isLoadingProceed, setIsLoadingProceed] = useState(false);
  const [error, setError] = useState("");
  const [marksConfigure, setmarksConfigure] = useState([]);
  const [showConfirmation, setShowConfirmation] = useState(false);

  useEffect(()=>{
    // console.log("DATA:");
    fetchSubjects();
  },[]);

  const fetchSubjects = async () =>{
    axios
    .get(`http://127.0.0.1:8000/api_v1/markings/${markings[0].subjectId}`)
    .then((response) => {
      const data = response.data
      setmarksConfigure(data.markConfig)
      // console.log("Data:",response.data.markConfig)
      setIsLoading(false);
      // Process the response data or update your React component state
    })
    .catch((error) => {
      console.error(error);
      setmarksConfigure(null)
      // Handle the error, e.g., display an error message to the user
    });
  }

  var length;
  var minimum;
  var maximum;

  const handleFormChange = (index, childFormData) => {
    // Update the form data for the specific child component
    const updatedFormData = [...marksConfigure];
    updatedFormData[index] = childFormData;
    if(index<marksConfigure.length-1){
      updatedFormData[index+1].minimum = updatedFormData[index].maximum+1;
    }
    setmarksConfigure(updatedFormData);
  };

  const handleAddChild = (index) => {
    // Add a new input fields to add ranges
    console.log("index",index)
    length=marksConfigure.length;
    minimum=marksConfigure[index].maximum+1;
    maximum=marksConfigure[index].maximum;
    const data = [...marksConfigure];
    const newdata = {
        "minimum" : minimum,
        "maximum" : maximum,
        "percentageOfMarks" : 0
    }

    data.splice(index+1,0,newdata);
    console.log("data::",data)

    setmarksConfigure(data);
  };

  const handleRemoveChild = (index) => {
    // Remove a range of input fields in the index
    const updatedFormData = [...marksConfigure];
    updatedFormData.splice(index, 1);
    if(index<marksConfigure.length-1){
      updatedFormData[index].minimum = updatedFormData[index-1].maximum;
    }
    setmarksConfigure(updatedFormData);
  };


  const handleIconClick = () => {
    setShowImages((prev) => !prev);
  };
  const handleProceedClose = () => {
    console.log("clicked")
    setShowConfirmation((prev) => !prev);
  };
  
 

  // const handleProceedClick = async () => {
  //   setError([])
  //   console.log("clicked")
  //   console.log("marksconfigure:::",marksConfigure)
  //   marksConfigure.forEach(async (markConfigure,index) => {
  //     if(markConfigure.maximum==="" || markConfigure.percentageOfMarks===""){
  //       setError("Please fill all the fields");
  //     }else if(index===(marksConfigure.length)-1){
  //       if(markConfigure.maximum!==100){
  //         setError("Range Should be 0-100.");
  //         // error.push("Range Should be 0-100.")

  //       }
  //     }else if(markConfigure.percentageOfMarks>100 || markConfigure.percentageOfMarks<0 || markConfigure.maximum>100 || markConfigure.maximum<0 || markConfigure.minimum>100 || markConfigure.minimum<0){
  //       console.log(markConfigure)
  //       setError(error=>[...error,"Please enter valid marks."]);
  //     }else if(markConfigure.maximum<=markConfigure.minimum){
  //       setError(error=>[...error,"Please enter valid range."]);

  //     }
  //   })
  //   console.log("errorrr:::",error)
  //   if(error?.length===0){
  //     setShowConfirmation(true);
  //   }
      //Ok link call
      // axios
      // .put(`http://127.0.0.1:8000/api_v1/markings/update/grading/${markings[0].markingScheme}`,marksConfigure)
      // .then((response) => {
      //   const data = response.data
      //   console.log("Data:",data)
      //   // setIsLoading(false);
      //   // Process the response data or update your React component state
      // })
      // .catch((error) => {
      //   console.error(error);
      //   setmarksConfigure(null)
      //   // Handle the error, e.g., display an error message to the user
      // });
    
  // }
  const handleProceedClick = async () => {
    setError("");
    console.log("clicked");
    // console.log("marksconfigure:::", marksConfigure);

    let hasError = false;

    for (const [index, markConfigure] of marksConfigure.entries()) {
      if (markConfigure.maximum === "" || markConfigure.percentageOfMarks === "") {
        setError("Please fill all the fields");
        hasError = true;
        break;
      } else if (index === marksConfigure.length - 1) {
        if (markConfigure.maximum !== 100) {
          setError("Range Should be 0-100.");
          hasError = true;
          break;
        }
      } else if (
        markConfigure.percentageOfMarks > 100 ||
        markConfigure.percentageOfMarks < 0 ||
        markConfigure.maximum > 100 ||
        markConfigure.maximum < 0 ||
        markConfigure.minimum > 100 ||
        markConfigure.minimum < 0
      ) {
        console.log(markConfigure);
        setError("Please enter valid marks.");
        hasError = true;
        break;
      } else if (markConfigure.maximum <= markConfigure.minimum) {
        setError("Please enter valid range.");
        hasError = true;
        break;
      }
    }

    console.log("errorrr:::", error);

    if (!hasError) {
      setShowConfirmation(true);
    }
};

const handleProceed = () => {
  //Methana isProcessed eka true wenna oona****************
  setShowConfirmation(false);
  console.log("clicked",isLoadingProceed)
  setIsLoadingProceed(prev=>!prev);
  console.log("clicked",isLoadingProceed)
  console.log("clicked:",markings[0].markingScheme)
  axios
  .put(`http://127.0.0.1:8000/api_v1/markings/update/grading/${markings[0].markingScheme}`,marksConfigure)
  .then((response) => {
    const data = response.data
    console.log("Data:",data)
    axios.patch(`http://127.0.0.1:8000/api_v1/answers/calculate_marks/${markings[0].markingScheme}/${markings[0].subjectId}`)
    .then((response)=>{
        console.log("Marks calculated:",response.data)
        setIsLoadingProceed(false);
        window.location.reload();
    })
    .catch((error)=>{
      console.log(error)
      alert("Something went wrong")
      setIsLoadingProceed(false);
    })
    // Process the response data or update your React component state
  })
  .catch((error) => {
    console.error(error);
    setmarksConfigure(null)
    setShowConfirmation(false);
    alert("Something went wrong")
    setIsLoadingProceed(false);
    // Handle the error, e.g., display an error message to the user
  });
}

  console.log(error)

  const handleOKClick = () => {
    setIsLoadingProceed(true);
    setError("");
    console.log("clicked");
    // console.log("marksconfigure:::", marksConfigure);

    let hasError = false;

    for (const [index, markConfigure] of marksConfigure.entries()) {
      console.log("<=:::",markConfigure.maximum <= markConfigure.minimum);
      if (markConfigure.maximum === "" || markConfigure.percentageOfMarks === "") {
        console.log("error1")
        setError("Please fill all the fields");
        hasError = true;
        break;
      } else if (index === marksConfigure.length - 1) {
        console.log("error2")
        if (markConfigure.maximum !== 100) {
          setError("Range Should be 0-100.");
          hasError = true;
          break;
        }else if (markConfigure.maximum <= markConfigure.minimum) {
          console.log("error4")
          setError("Please enter valid range.");
          hasError = true;
          break;
        }
      } else if (
        markConfigure.percentageOfMarks > 100 ||
        markConfigure.percentageOfMarks < 0 ||
        markConfigure.maximum > 100 ||
        markConfigure.maximum < 0 ||
        markConfigure.minimum > 100 ||
        markConfigure.minimum < 0 
      ) {
        console.log("error3")
        setError("Please enter valid marks.");
        hasError = true;
        break;
      } else if (markConfigure.maximum <= markConfigure.minimum) {
        console.log("error4")
        setError("Please enter valid range.");
        hasError = true;
        break;
      }
    }

    console.log("errorrr:::", error);

    if (!hasError) {
      axios
      .put(`http://127.0.0.1:8000/api_v1/markings/update/grading/${markings[0].markingScheme}`,marksConfigure)
      .then((response) => {
        const data = response.data
        console.log("Data:",data)
        setIsLoadingProceed(false);
        window.location.reload();
        // setIsLoading(false);
        // Process the response data or update your React component state
      })
      .catch((error) => {
        console.error(error);
        setmarksConfigure(null)
        setIsLoadingProceed(false);
        alert("Something went wrong")
        // Handle the error, e.g., display an error message to the user
      });
    }
    
  }


  const data = answers.map((answer, index) => (
      markings[index].selected && (<MarksBox
        key={answer.id}
        markingScheme_URL={markings[index].uploadUrl}
        answersheet_URL={answer.uploadUrl}
        answer={answer}
        marking={markings[index]}
        showImages={showImages}
      />)
      // console.log(markings[index])
    ));

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Configure Marks</p>
      <p className="text-center font-medium">Add marks allocated for each range(mark for student's answer obtained accuracy)</p>
      {/* <button onClick={handleIconClick}>View All</button> */}
      <div className="flex flex-col items-center mb-16">
        <div>
          {isLoading ? <MoonLoader color="#4457FF" loading={isLoading} size={50} /> :
            <MarkAccurcyConfigure marksConfigure={marksConfigure} handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} handleFormChange={handleFormChange} error={error}/>
          }
        </div>
        <div className="flex flex-row">
          <Button onClick={handleOKClick} classNames="w-24 text-center bg-custom-blue-main mt-2 mr-2">Ok</Button>
          <Button onClick={handleProceedClick} classNames="w-24 text-center bg-custom-blue-main mt-2">Proceed</Button>
        </div>
      </div>
      {
        showImages ? <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-main absolute left-[85%] mt-2">Hide All</Button>
        : <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-main absolute left-[85%] mt-2">View All</Button>
      }
      {isLoading ? <MoonLoader color="#4457FF" loading={isLoading} size={50} className='absolute top-[5vw] left-[45%]'/> :
        data
      }

      {isLoadingProceed ? <MoonLoader color="#4457FF" loading={isLoadingProceed} size={50} className='absolute top-[8vw] left-[50%]'/> : ""}

      {showConfirmation && <Modal handleProceed={handleProceed} onClose={handleProceedClose}/>}
    </div>
  )
}

export default Marks
