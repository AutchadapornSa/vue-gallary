// export const images = [
//     {
//       id: 1,
//       url: "https://picsum.photos/400/300?random=1",
//       hashtags: ["#nature", "#mountain"]
//     },
//     {
//       id: 2,
//       url: "https://picsum.photos/400/300?random=2",
//       hashtags: ["#city", "#night"]
//     },
//     {
//       id: 3,
//       url: "https://picsum.photos/400/300?random=3",
//       hashtags: ["#beach", "#sunset"]
//     }
//   ]
export const images = Array.from({ length: 50 }, (_, i) => ({
    id: i + 1,
    url: `https://picsum.photos/${300 + (i % 100)}/${200 + (i % 100)}?random=${i + 1}`,
    hashtags: Array.from({ length: Math.floor(Math.random() * 6) + 1 }, (_, j) => `#tag${j + 1}`)
  }))