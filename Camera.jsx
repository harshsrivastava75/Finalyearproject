import { useEffect, useRef } from "react";

export default function Camera() {
  const videoRef = useRef(null);

  useEffect(() => {
    async function startCamera() {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      videoRef.current.srcObject = stream;
    }

    startCamera();
  }, []);

  return (
    <div className="bg-gray-800 rounded-xl p-5">
      <h2 className="text-xl mb-4">Live Face Detection</h2>

      <video
        ref={videoRef}
        autoPlay
        playsInline
        className="w-full h-72 rounded-lg bg-black object-cover"
      />

      <button className="bg-green-600 mt-5 p-3 rounded w-full">
        Start Recognition
      </button>
    </div>
  );
}