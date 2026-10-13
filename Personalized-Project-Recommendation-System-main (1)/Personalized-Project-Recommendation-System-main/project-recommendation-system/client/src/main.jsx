import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
<div className="max-w-7xl mx-auto p-8">

    <h1 className="text-4xl font-bold text-center text-blue-700">
        Personalized Project Recommendation System
    </h1>

    <p className="text-center text-gray-600 mt-2">
        Discover software projects tailored to your interests and career goals.
    </p>

</div>
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
