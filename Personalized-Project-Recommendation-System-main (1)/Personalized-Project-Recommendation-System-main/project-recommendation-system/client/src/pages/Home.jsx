import { useState } from "react";
import api from "../services/api";

function Home() {

    const [domain, setDomain] = useState("");
    const [difficulty, setDifficulty] = useState("");
    const [duration, setDuration] = useState("");
    const [technologies, setTechnologies] = useState("");
    const [careerGoal, setCareerGoal] = useState("");
    const [interests, setInterests] = useState("");
    const [experience, setExperience] = useState("");
    const [teamPreference, setTeamPreference] = useState("");

    const [loading, setLoading] = useState(false);
    const [result, setResult] = useState(null);

    const handleRecommend = async () => {

        try {

            setLoading(true);

            const response = await api.post("/recommend", {

                domain,
                difficulty,
                duration,
                technologies,
                career_goal: careerGoal,
                interests,
                required_experience: experience,
                team_preference: teamPreference

            });

            setResult(response.data);

        } catch (error) {

            console.error(error);

        } finally {

            setLoading(false);

        }

    };

   return (
  <div className="min-h-screen bg-slate-100">
    <div className="max-w-7xl mx-auto p-8">

      <h1 className="text-4xl font-bold text-center text-blue-700">
        Personalized Project Recommendation System
      </h1>

      <p className="text-center text-gray-600 mt-2">
        Discover software projects tailored to your interests and career goals.
      </p>
      <div className="mt-10 grid grid-cols-2 gap-6">

    <select
        className="border p-3 rounded-lg"
        value={domain}
        onChange={(e)=>setDomain(e.target.value)}
    >
        <option value="">Select Domain</option>
        <option>Artificial Intelligence</option>
        <option>Cybersecurity</option>
        <option>Web Development</option>
        <option>Data Science</option>
        <option>Mobile Development</option>
    </select>

    <select
        className="border p-3 rounded-lg"
        value={difficulty}
        onChange={(e)=>setDifficulty(e.target.value)}
    >
        <option value="">Difficulty</option>
        <option>Beginner</option>
        <option>Intermediate</option>
        <option>Advanced</option>
    </select>

    <select
        className="border p-3 rounded-lg"
        value={duration}
        onChange={(e)=>setDuration(e.target.value)}
    >
        <option value="">Duration</option>
        <option>1 Month</option>
        <option>2 Months</option>
        <option>3 Months</option>
        <option>6 Months</option>
    </select>

    <input
        className="border p-3 rounded-lg"
        placeholder="Technologies (Python, React...)"
        value={technologies}
        onChange={(e)=>setTechnologies(e.target.value)}
    />

    <select
        className="border p-3 rounded-lg"
        value={careerGoal}
        onChange={(e)=>setCareerGoal(e.target.value)}
    >
        <option value="">Career Goal</option>
        <option>Placement Preparation</option>
        <option>Portfolio Building</option>
        <option>Higher Studies</option>
        <option>Research</option>
        <option>Startup</option>
    </select>

    <select
        className="border p-3 rounded-lg"
        value={experience}
        onChange={(e)=>setExperience(e.target.value)}
    >
        <option value="">Experience</option>
        <option>Beginner</option>
        <option>Beginner to Intermediate</option>
        <option>Intermediate</option>
        <option>Intermediate to Advanced</option>
        <option>Advanced</option>
    </select>

    <select
        className="border p-3 rounded-lg"
        value={teamPreference}
        onChange={(e)=>setTeamPreference(e.target.value)}
    >
        <option value="">Team Preference</option>
        <option>Individual</option>
        <option>Team</option>
        <option>Both</option>
    </select>

    <input
        className="border p-3 rounded-lg"
        placeholder="Interests (AI, Healthcare...)"
        value={interests}
        onChange={(e)=>setInterests(e.target.value)}
    />
    <div className="mt-8 text-center">

    <button
        onClick={handleRecommend}
        disabled={loading}
        className="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 disabled:bg-gray-400"
    >
        {loading ? "Finding Best Projects..." : "Get Recommendations"}
    </button>
{result && (

<div className="mt-10">

    <h2 className="text-3xl font-bold mb-6">
        Recommended Projects
    </h2>

    <div className="grid md:grid-cols-2 gap-6">

        {result.recommended_projects.map((project,index)=>(

            <div
                key={index}
                className="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition"
            >

                <h3 className="text-xl font-bold text-blue-700">
                    {project.title}
                </h3>

                <p className="mt-2">
                    ⭐ Score :
                    <span className="font-semibold">
                        {" "}
                        {project.similarity_score}
                    </span>
                </p>

                <p className="mt-2">
                    📂 <b>Domain:</b> {project.domain}
                </p>

                <p>
                    📈 <b>Difficulty:</b> {project.difficulty}
                </p>

                <p>
                    ⏱ <b>Duration:</b> {project.duration}
                </p>

                <p>
                    💻 <b>Technologies:</b>
                    {" "}
                    {project.technologies}
                </p>

                <p className="mt-3 text-gray-600">
                    {project.description}
                </p>

            </div>

        ))}

    </div>

</div>

)}
</div>
{result && (

<div className="mt-10 bg-white rounded-xl shadow-lg p-6">

    <h2 className="text-3xl font-bold text-blue-700 mb-4">

        🤖 AI Mentor

    </h2>

    <div className="whitespace-pre-wrap text-gray-700">

        {result.ai_explanation}

    </div>

</div>

)}

</div>

    </div>
  </div>
);

}

export default Home;