import { useState,useRef,useCallback } from 'react';
import {useDropzone} from 'react-dropzone';
import { AiOutlinePlus, AiOutlineClose,AiOutlineUpload} from "react-icons/ai";
import  ReactDOM  from 'react-dom';
import { Link ,useLocation, useParams } from 'react-router-dom';
import axios from 'axios'
function DragDrop({children,closeFunc}) {
  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')

  //Get parameters
  const {year,subjectId} = useParams();
  console.log(year);
  console.log(subjectId);
  console.log(pathName[0]);
  const [files ,setFiles] =useState([]);

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
    e.preventDefault();
    if(!files?.length) return
    const formData = new FormData()
    files.forEach(file => formData.append('file', file))
    console.log(formData)
    

    let response = []
    try{
      if(pathName[0]==="markingschemes"){
        formData.append('year', year);
        formData.append('subjectId',subjectId);
        response = axios.post(`http://127.0.0.1:8000/api_v1/markings`,formData);
      }else if(pathName[0]==="answersheets"){
        formData.append('year', year);
        formData.append('subjectId',subjectId);
        response = axios.post(`http://127.0.0.1:8000/api_v1/papers/upload/file`,formData);
      }
      console.log(response);
    }catch(error){
      // console.log("error:"+error.response.data.message);
      if(error.response && error.response.status >=400 && error.response.status <500){
          // console.log(error.response.data.message);
          console.log(error.response.data.message);
      }
  }

  
  }

  console.log(files);
  return ReactDOM.createPortal(
    <div >
      <div className='z-30 fixed inset-0 bg-gray-300 opacity-80' onClick={closeFunc}></div>
      <div className='z-30 absolute top-[10%] left-[35%] h-fit w-fit p-5 bg-white  flex flex-col items-center max-lg:left-[20%]'>
          <div className='w-full flex justify-end'>
            <AiOutlineClose onClick={closeFunc} className='cursor-pointer -mb-12 text-white text-center text-3xl bg-red-400 rounded-xl p-1 hover:bg-red-500'/>
          </div>
          <p className= "flex items-center justify-center ml-8 mt-11 text-2xl font-bold text-#2e1065 md:text-2xl dark:text-#2e1065 pt-10 " >{children}</p>
          <p className="flex items-center justify-center mt-2 ml-8 text-lg font-semibold text-inherit md:text-lg dark:text-inherit ">Upload your {children} (Paper should be according to our structure)</p>
      <div className="flex flex-col w-[90%] justify-center items-center">
      {/* Drop Box */}
        <form onSubmit={handleSubmit} className=' flex flex-col items-center justify-center w-[95%]'>  
            <div {...getRootProps()} className="border border-green-600 py-6 flex flex-col inset-y-5 right-0 items-center justify-center box-border h-max w-[90%] m-12 px-4 mtransition bg-blue-700 rounded-lg">
              <input {...getInputProps()} multiple/>

              <div className="relative flex justify-center box-border h-max w-[90%] border-2 border-white  border-dashed rounded-md appearance-none cursor-pointer hover:border-gray-400 focus:outline-none py-4">

                  <div className="absolute text-center box-border pt-0 w-[100%] text-xl font-bold text-white font-roboto p-5">
                      {children}
                  </div>
                  <div className="mt-10 flex flex-col items-center justify-center w-full text-center relative text-lg font-roboto w-[90%] inset-x-0 top-0 text-white mt-13">
                      <div>
                        {
                        isDragActive ?
                          <p>Drop the files here ...</p> :
                          <p>Drag 'n' drop some files here, or click to select files</p>
                        }
                      </div>
                      <div className="mt-4 flex flex-col items-center justify-center ">
                        <button className="mb-4 w-40 max-sm:w-24 bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded inline-flex items-center" ><AiOutlinePlus/>Choose Files</button>

                      </div>
                  </div>
              </div>
            </div>
          <button type='submit' className="mb-4 w-40 max-sm:w-24 bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded flex justify-center text-center items-center" ><AiOutlineUpload/>Upload</button>
        </form>  
            <ul className='list-disc w-fit'>
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

