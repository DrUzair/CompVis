def pca_saliency(image, col_space='LAB'):
    # image_lab = rgb2lab(image)
    # image_lab = (image_lab + [0, 128, 128]) / [100, 255, 255] # https://stackoverflow.com/questions/46415948/converting-rgb-images-to-lab-using-scikit-image
    #image_cv2 = cv2.imread('ManOnWall.jpg', 1)
    if col_space=='LAB':
        image_int = image.astype(np.uint8)
        image_lab = np.float32(cv2.cvtColor(image_int, cv2.COLOR_BGR2LAB))
        image_lab[:, :, 0] = (image_lab[:, :, 0] - 0.) / (255. - 0.)
        image_lab[:, :, 1] = (image_lab[:, :, 1] - 42.) / (226. - 42.)
        image_lab[:, :, 2] = (image_lab[:, :, 2] - 20.) / (223. - 20.)
        image = image_lab

    Feat = [image]
    numFeat = len(Feat)
    height, width, _ = Feat[0].shape
    SalMap = np.zeros((height, width), dtype=np.float32)
    for F in range(numFeat):
        dimFeat = Feat[F].shape[2]
        feat = np.reshape(Feat[F], (height * width, dimFeat), order='F')  # [height*width, dimFeat]
        # Get the principal components and represent the feature in the PCA coordinate system
        pca = PCA(n_components=None)  # preserve all the components
        pca.fit(feat)
        # print( pca.components_)
        # print(pca.components_.shape)
        FeatPCAed = pca.transform(feat)  # [height*width,NumComponents]
        del feat, pca

        SalMap_L = np.sum(abs(FeatPCAed), axis=1)  # [height*width,1]
        del FeatPCAed

        # Normalize to range between 0 and 1
        SalMap_L = (SalMap_L - SalMap_L.min()) / (SalMap_L.max() - SalMap_L.min())

        SalMap[:, :] = np.reshape(SalMap_L, (height, width), order='F')
