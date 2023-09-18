import { useState,useRef,useCallback } from 'react';
import {useDropzone} from 'react-dropzone';
import { AiOutlinePlus, AiOutlineClose,AiOutlineUpload} from "react-icons/ai";
import  ReactDOM  from 'react-dom';
import { Link ,useLocation, useParams ,useNavigate} from 'react-router-dom';
import { BarLoader } from 'react-spinners';
import axios from 'axios'
function DragDrop({children,closeFunc,data}) {
  const navigate = useNavigate();
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')

  //Get parameters
  const {year,subjectId} = useParams();
  console.log(year);
  console.log(subjectId);
  console.log(pathName[0]);
  const [files ,setFiles] =useState([]);
  // const [paper, setPaper] = useState("");

  const [uploading, setUploading] = useState(false);

  const onDrop = useCallback(acceptedFiles => {
    // Do something with the files
    if(acceptedFiles?.length){
      // console.log(acceptedFiles);
      setFiles(previousFiles=>[
        ...previousFiles,
        ...acceptedFiles.map(file=>
          Object.assign(file,{preview : URL.createObjectURL(file)})
          )
        ])
      }
      const formData = new FormData();
      
      acceptedFiles.forEach((file) => {
        formData.append('files', file);
      });
      // console.log(files);
    console.log(formData);
  }, [])
  const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop})

  const removeFile = (name) =>{
    setFiles(files => files.filter(file =>file.name !== name))
    // console.log(files);
  }

  const handleSubmit = (e) =>{
    let paper;
    let index;
    e.preventDefault();
    if(!files?.length) return
    const formData = new FormData()
    files.forEach(file => formData.append('files', file))
    formData.append('year', year);
    formData.append('subjectId',subjectId);
    console.log("form data",formData.get('files'))
    setUploading(true);
    if(pathName[0]==="markingschemes"){
      axios
      .post(`http://127.0.0.1:8000/api_v1/markings`,formData)
      .then((response) => {
        console.log("Dinith:",response);
        localStorage.setItem('markingSceme', JSON.stringify(response.data));
        setUploading(false);
        closeFunc()
        window.location.reload();

      })
      .catch((error) => {
        if(error.response && error.response.status >=400 && error.response.status <500){
          // console.log(error.response.data.message);
          console.log(error.response.data.detail);
          setUploading(false);
          closeFunc()
          alert('Something went wrong')
          window.location.reload();
      }
      });
    }
    else if(pathName[0]==="answersheets"){
      axios
      .post(`http://127.0.0.1:8000/api_v1/papers/upload/file`,formData)
      .then((response) => {
        console.log("Hello:",response.data);
        setUploading(false);
        closeFunc()
        window.location.reload();
        // console.log(index)
        // for (const [index, paper] of papers.entries()){
      })
      .catch((error) => {
        if(error.response && error.response.status >=400 && error.response.status <500){
          // console.log(error.response.data.message);
          console.log(error.response.data.detail);
          // alert('Something went wrong')
          setUploading(false);
          closeFunc()
          alert('Something went wrong')
          window.location.reload();
      }
      });
    }
    // console.log("error:"+error.response.data.message);
  }

  console.log(files);
  return ReactDOM.createPortal(
    <div className='flex justify-center items-center'>
      <div className='z-30 fixed inset-0 opacity-70 bg-gray-500 flex items-center justify-center' onClick={closeFunc}></div>
      <div className='z-30 absolute top-0 left-0 h-full w-full p-5 bg-white  flex flex-col items-center max-sm:top-[10%]'>
          <div className='fixed right-6 w-full flex justify-end'>
            <AiOutlineClose onClick={closeFunc} className='cursor-pointer -mb-12 text-white text-center text-3xl bg-red-400 rounded-xl p-1 hover:bg-red-500'/>
          </div>
          <p className= "flex items-center justify-center ml-8 mt-11 text-2xl font-bold text-[#191854] md:text-2xl dark:text-#2e1065 pt-10 " >{children}</p>
          <p className="flex items-center justify-center mt-2 ml-8 text-lg font-semibold text-inherit md:text-lg dark:text-inherit ">Upload your {children} (Paper should be according to our structure)</p>
          {
            pathName[0]==="markingschemes" ?
              data!==null ?
                <p className="text-center text-lg font-semibold text-red-600">*Previous marking scheme will replaced</p>
              : ''
            : ''
          }
      <div className="flex flex-col w-[90%] mt-8 h-[60%] justify-center items-center">
      {/* Drop Box */}
        <form onSubmit={handleSubmit} className='h-full flex flex-col items-center justify-center w-[95%]'>  
            <div {...getRootProps()} className="h-full py-6 flex flex-col inset-y-5 right-0 items-center justify-center box-border w-[90%] m-12 px-4 mtransition bg-[#D4D4D4] rounded-lg">
              <input {...getInputProps()} multiple/>

              <div className="h-full relative flex justify-center box-border w-[90%] border-2 border-white  border-dashed rounded-md appearance-none cursor-pointer hover:border-gray-400 focus:outline-none py-4">

                  <div className="absolute text-center box-border pt-0 w-[100%] text-xl font-bold text-white font-roboto p-5">
                      {children}
                  </div>
                  <div className="mt-10 flex flex-col items-center justify-center w-full text-center relative text-lg font-roboto inset-x-0 top-0 text-white mt-13">
                      <div>
                        {
                        isDragActive ?
                          <p>Drop the files here ...</p> :
                          <p>Drag 'n' drop some files here, or click to select files</p>
                        }
                        
                      </div>
                      <div className="mt-4 flex flex-col items-center justify-center ">
                        <button className="mb-4 w-40 max-sm:w-24 bg-white hover:opacity-90 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center" ><AiOutlinePlus/>Choose Files</button>

                      </div>
                  </div>
              </div>
            </div>
            {uploading && <div><BarLoader color="#3443C9" height={6} width={256} /></div>}
          <button type='submit' className="my-8 w-fit max-sm:w-24 bg-[#3443C9] hover:opacity-90 text-white font-bold py-2 rounded flex gap-2 px-[8%] justify-center text-center items-center " ><AiOutlineUpload/>Upload {children}</button>
        </form>  
            <ul className='list-disc w-fit mt-8'>
              {files.map(file => (
                <li key={file.name}>
                  <div className="flex flex-row justify-between mb-2">
                      <p className=" text-left text-lg font-semibold text-#2e1065 md:text-lg dark:text-#2e1065">{file.name}&nbsp;</p>
                      {/* <p className=" text-left text-lg font-semibold text-#2e1065 md:text-lg dark:text-#2e1065">{file.path}&nbsp;</p> */}
                      <button type="button" className='ml-5 text-white text-center bg-red-400 rounded-xl p-1 hover:bg-red-500' onClick={()=>removeFile(file.name)}><AiOutlineClose/></button>
                  </div>
                </li>
              ))}
            </ul>
      {/* Drop Box End*/}
       </div>
       <p className= "flex items-center justify-center ml-8 mt-0 text-2xl font-bold text-#2e1065 md:text-2xl dark:text-#2e1065 pt-10 " >
        {/* <span><button className="h-10 w-96 text-lg text-white bg-#2563eb hover:bg-#2563eb focus:ring-4 focus:ring-blue-300 font-semibold rounded-lg  mb-16 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
          Check Answers
          </button>
          </span> */}
        </p>

        {/* preview */}
        

      </div>
    </div>,
    document.querySelector('.modal-container')
  )
}

export default DragDrop;

