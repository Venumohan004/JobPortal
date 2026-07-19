import Navbar from "../components/common/Navbar";
import Hero from "../components/home/Hero";
import SearchSection from "../components/home/SearchSection";
import FeaturedJobs from "../components/home/FeaturedJobs";
import Footer from "../components/common/Footer";
import Stats from "../components/home/Stats";

function Home() {
  return (
    <>
      {/* <Navbar /> */}
      <Hero />
      <SearchSection />
      <FeaturedJobs />
      <Stats />
      <Footer />
    </>
  );
}

export default Home;