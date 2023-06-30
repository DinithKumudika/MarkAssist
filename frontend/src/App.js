import { Route, Routes } from 'react-router-dom';
import TopBar from "./Components/TopBar";
import QuestionsPage from "./Pages/QuestionsPage";
import EssayPage from './Pages/EssayPage';
import McqPage from './Pages/McqPage';
import './Components/TopBar.css';
import TeacherPage from './Pages/TeacherPage';

function App(){
  return(
    <div>
      {/* <TopBar /> */}
      <Routes>
        <Route path="/" element={<QuestionsPage />} />
        <Route path="essayPage" element={<EssayPage />} />
        <Route path="mcqPage" element={<McqPage />} />
        <Route path="teacherPage" element={<TeacherPage />} />
      </Routes>
    </div>
  );
}

export default App;
