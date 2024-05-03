import librosa
import numpy as np
import scipy.ndimage


def compute_spectrogram(fn_wav, Fs=22050, N=2048, H=1024, bin_max=128, frame_max=None, duration = None, offset = 1):
    x, Fs = librosa.load(fn_wav, sr=Fs, offset = offset, duration = duration)
    x_duration = len(x) / Fs
    X = librosa.stft(x, n_fft=N, hop_length=H, win_length=N, window='hamming')
    if bin_max is None:
        bin_max = X.shape[0]
    if frame_max is None:
        frame_max = X.shape[0]
    Y = np.abs(X[:bin_max, :frame_max])
    return Y

def compute_constellation_map(Y, dist_freq=3, dist_time=3, thresh=0.01):
    """Compute constellation map (implementation using image processing)
    Args:
        Y (np.ndarray): Spectrogram (magnitude)
        dist_freq (int): Neighborhood parameter for frequency direction (kappa) (Default value = 7)
        dist_time (int): Neighborhood parameter for time direction (tau) (Default value = 7)
        thresh (float): Threshold parameter for minimal peak magnitude (Default value = 0.01)

    Returns:
        Cmap (np.ndarray): Boolean mask for peak structure (same size as Y)
    """
    result = scipy.ndimage.maximum_filter(Y, size=[2*dist_freq+1, 2*dist_time+1], mode='constant')
    Cmap = np.logical_and(Y == result, result > thresh)
    return Cmap

def compare (val, val2):
    count = 0
    for el in val:
        if el in val2:
            count += 1
    return count

def hash(k, n):
    data = []
    for idx in range(len(k)-1):
        data.append((k[idx], k[idx + 1], n[idx+1] - n[idx]))
    return data

def constellation_map(Cmap, Y=None, xlim=None, ylim=None):

    """Plot constellation map
    Args:
        Cmap: Constellation map given as boolean mask for peak structure
        Y: Spectrogram representation (Default value = None)

    Returns:
        k:  The frequency's coordinate of peak
        n:  The time's coordinate of peak
    """
    if Cmap.ndim > 1:
        (K, N) = Cmap.shape
    else:
        K = Cmap.shape[0]
        N = 1
    if Y is None:
        Y = np.zeros((K, N))
    Fs = 1
    n, k = np.argwhere(Cmap == 1).T
    return k, n


