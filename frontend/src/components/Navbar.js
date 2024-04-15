import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="bg-gray-700 text-white py-4 shadow-md">
      <div className="container mx-auto px-4 flex justify-between items-center">
        <Link to="/" className="text-white text-3xl font-bold no-underline">
          News
        </Link>
        <nav>
          <ul className="flex gap-4">
            <li>
              <Link
                to="/about"
                className="text-lg text-gray-100 hover:text-gray-500 transition-colors duration-300"
              >
                About
              </Link>
            </li>
            <li>
              <Link
                to="/contact"
                className="text-lg text-gray-100 hover:text-gray-500 transition-colors duration-300"
              >
                Contact
              </Link>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Navbar;
