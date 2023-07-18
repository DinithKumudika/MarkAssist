import MarksBox from "./MarksBox"
import Button from "../Button"
import MarkAccurcyConfigure from "./MarkAccurcyConfigure"
import classnames from 'classnames';
import { useState , useEffect } from 'react'
import { MoonLoader } from 'react-spinners';
import axios from "axios";
function Marks({clicked,answers,markings}) {
  const classes = classnames('sidebar static max-sm:ml-16 pt-[80px]');
  // const answersheets = JSON.parse(localStorage.getItem('answers'));
  // const markingschemes = JSON.parse(localStorage.getItem('markingSceme'));
  // console.log(answers)
  // console.log(markings)
  const [showImages, setShowImages] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");
  const [marksConfigure, setmarksConfigure] = useState([]);

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
      console.log("Data:",response.data.markConfig)
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

  const handleFormChange = (index, childFormData) => {
    // Update the form data for the specific child component
    const updatedFormData = [...marksConfigure];
    updatedFormData[index] = childFormData;
    if(index<marksConfigure.length-1){
      updatedFormData[index+1].minimum = updatedFormData[index].maximum;
    }
    setmarksConfigure(updatedFormData);
  };

  const handleAddChild = () => {
    // Add a new input fields to add ranges
    length=marksConfigure.length;
    minimum=marksConfigure[length-1].maximum;
    setmarksConfigure([...marksConfigure, 
      {
        "minimum" : minimum,
        "maximum" : null,
        "marks" : null
      }
    ]);
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

  const handleProceedClick = () => {
    console.log(marksConfigure)
    marksConfigure.map((markConfigure,index) => {
      if(markConfigure.maximum==="" || markConfigure.percentageOfMarks===""){
        setError("Please fill all the fields")
      }else if(index===marksConfigure.length-1){
        if(markConfigure.maximum!==100){
          setError("Range Should be 0-100.")
        }
      }else if(markConfigure.percentageOfMarks>100 || markConfigure.percentageOfMarks<0 || markConfigure.maximum>100 || markConfigure.maximum<0 || markConfigure.minimum>100 || markConfigure.minimum<0){
        console.log(markConfigure)
        setError("Please enter valid marks.")
      }else if(markConfigure.maximum<=markConfigure.minimum){
        setError("Please enter valid range.")
      }else{
        setError("")
      }
      if(error===""){
        //Proceed link call
        console.log("Proceed",marksConfigure)
        return 1;
      }else{
        return 0;
      }
    })
  }
  console.log(error)

  const handleOKClick = () => {
    marksConfigure.map((markConfigure,index) => {
      if(markConfigure.maximum==="" || markConfigure.percentageOfMarks===""){
        setError("Please fill all the fields")
      }else if(markConfigure.marks>100 || markConfigure.percentageOfMarks<0 || markConfigure.maximum>100 || markConfigure.maximum<0 || markConfigure.minimum>100 || markConfigure.minimum<0){
        console.log(markConfigure)
        setError("Please enter valid marks.")
      }else if(markConfigure.maximum<=markConfigure.minimum){
        setError("Please enter valid range.")
      }else{
        setError("")
      }
      if(error===""){
        //Ok link call
        axios
        .put(`http://127.0.0.1:8000/api_v1/markings/update/grading/${markings[0].markingScheme}`,marksConfigure)
        .then((response) => {
          const data = response.data
          console.log("Data:",data)
          // setIsLoading(false);
          // Process the response data or update your React component state
        })
        .catch((error) => {
          console.error(error);
          setmarksConfigure(null)
          // Handle the error, e.g., display an error message to the user
        });
        return 1;
      }else{
        return 0;
      }
    })
  }


  const data = answers.map((answer, index) => (
      <MarksBox
        key={answer.id}
        markingScheme_URL={markings[index].uploadUrl}
        answersheet_URL={answer.uploadUrl}
        answer={answer}
        marking={markings[index]}
        showImages={showImages}
      />
      // console.log(markings[index])
    ));

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <p className="text-center text-[#191854] text-xl font-bold">Configure Marks</p>
      <p className="text-center font-medium">Add marks allocated for each range(mark for student's answer obtained accuracy)</p>
      {/* <button onClick={handleIconClick}>View All</button> */}
      <div className="flex flex-col items-center mb-16">
        <div>
          {isLoading ? <MoonLoader color="#191854" loading={isLoading} size={50} /> :
            <MarkAccurcyConfigure marksConfigure={marksConfigure} handleAddChild={handleAddChild} handleRemoveChild={handleRemoveChild} handleFormChange={handleFormChange} error={error}/>
          }
        </div>
        <div className="flex flex-row">
          <Button onClick={handleOKClick} classNames="w-24 text-center bg-custom-blue-2 mt-2 mr-2">Ok</Button>
          <Button onClick={handleProceedClick} classNames="w-24 text-center bg-custom-blue-2 mt-2">Proceed</Button>
        </div>
      </div>
      {
        showImages ? <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">Hide All</Button>
        : <Button onClick={handleIconClick} classNames="w-24 text-center bg-custom-blue-2 absolute left-[85%] mt-2">View All</Button>
      }
      {isLoading ? <MoonLoader color="#191854" loading={isLoading} size={50} /> :
        data
      }
    </div>
  )
}

export default Marks
