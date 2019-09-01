import imageio
images = []

for e in range(100):
    img_name = 'MNIST_GAN_results/results/MNIST_GAN_' + str(e + 1) + '.png'
    images.append(imageio.imread(img_name))
imageio.mimsave('MNIST_GAN_results/generation_animation.gif', images, fps=5)

images = []

for e in range(100):
    img_name = 'MNIST_GAN_results/withoutdropout_results/MNIST_GAN_' + str(e + 1) + '.png'
    images.append(imageio.imread(img_name))
imageio.mimsave('MNIST_GAN_results/withoutdropoout_generation_animation.gif', images, fps=5)