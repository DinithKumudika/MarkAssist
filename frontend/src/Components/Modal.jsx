import ReactDOM from 'react-dom'
import { AiOutlinePlus, AiOutlineClose,AiOutlineUpload} from "react-icons/ai";
function Modal({onClose,handleProceed,handleLink,message,clicked}) {
    return ReactDOM.createPortal(
        <div className='flex justify-center items-center'>
          <div className='z-30 fixed inset-0 bg-gray-300 opacity-80 flex items-center justify-center' onClick={onClose && onClose}></div>
          <div className={`z-30 fixed top-[40%] m-[auto] h-fit w-fit p-5 bg-white  flex flex-col items-center max-sm:top-[10%] `}>
            <div className='flex flex-col'>
                {onClose && (<div className='flex justify-end'>
                    <AiOutlineClose onClick={onClose} className='mb-2 cursor-pointer text-white text-center text-3xl bg-red-400 rounded-xl p-1 hover:bg-red-500'/>
                </div>)}
                {message ? <h2>{message}</h2> : <h2>Are you sure you want to proceed. This cannot be un done.</h2>}
                <div className='p-4 flex items-center justify-center gap-2'>
                    {handleProceed && <button onClick={handleProceed} className='border-2 p-2 rounded-lg bg-custom-blue-2 text-white font-bold'>OK</button>}
                    {onClose && <button onClick={onClose} className='border-2 p-2 rounded-lg bg-custom-blue-2 text-white font-bold'>Close</button>}
                    {handleLink && <button onClick={handleLink} className='border-2 p-2 rounded-lg bg-custom-blue-2 text-white font-bold'>Go</button>}
                </div>
            </div>

          </div>
          
        </div>,
        document.querySelector('.modal-container')
      )
}

export default Modal
