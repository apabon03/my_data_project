import { BrowserRouter, Routes, Routem, Navigate } from 'react-router-dom'
import { FilePages } from './pages/FilePages'
import { LogingPages } from './pages/LogingPages'
import { FileFormPages } from './pages/FileFormPages'
import { LogupPages } from './pages/LogupPages'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/files"/>}/>
        <Route path="/logup" element={<LogupPages/>}/>
        <Route path="/login" element={<LogingPages/>}/>
        <Route path="/files" element={<FilePages/>}/>
        <Route path="/up_files" element={<FileFormPages/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App